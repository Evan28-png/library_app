from flask import Flask, redirect, render_template, request, url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, EmailField, PasswordField
from wtforms.validators import Email, InputRequired
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import bcrypt
from flask_login import UserMixin
import pymysql

app = Flask(__name__)
app.config['SECRET_KEY'] = 'HARD TO GUESS STRING'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://evan:Pierreevan@localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False
db = SQLAlchemy(app)

#Models
association_table = db.Table(
        'association',
        db.Column('book_id', db.ForeignKey('books.id'), primary_key=True),
        db.Column('author_id', db.ForeignKey('authors.id'), primary_key=True),
        )
migrate = Migrate(app, db)

class Books(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(34), index=True)
    category = db.Column(db.String(32))
    authors = db.relationship('Author', secondary=association_table, back_populates='books')

    def __str__(self):
        return f'{self.id}, {self.title}'


class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index=True)
    books = db.relationship('Books', secondary=association_table, back_populates='authors')

    def __str__(self):
        return f'{self.name}'


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(32), index=True)
    lname = db.Column(db.String(32), index=True)
    pass_hash = db.Column(db.String(128))
    
    @property
    def password(self):
        raise AttributeError

    @password.setter
    def password(self, password):
        self.pass_hash = bcrypt.generate_password_hash(password)

    def verify_pass_hash(self, password):
        return bcrypt.check_password_hash(self.pass_hash, password)





class Registrationform(FlaskForm):
    fname = StringField('First name', [InputRequired()])
    lname = StringField('Last name', [InputRequired()])
    email = EmailField('Email', [InputRequired()])
    password = PasswordField('Enter password', [InputRequired()])
    submit = SubmitField('Submit')


#class Loginform(FlaskForm):
#    email = EmailField('Enter login email')
#    password = PasswordField('Enter password')



@app.route('/')
def index():
    #return "it is working"
    try:
        books = Books.query.all()
    except Exception as e:
        print(f'error in book.query{e}')
    return render_template('index.html', books=books)


@app.route('/book')
def borrow():
    book_id = request.args.get('book_id')
    book = Books.query.filter_by(id=book_id).first()
    return render_template('borrow.html', book=book)

@app.route('/all_books')
def all_books():
    auth_id = request.args.get('author_id')
    author = Author.query.filter_by(id=auth_id).first()
    return render_template('all_books.html', author=author)


@app.route('/registration', methods=['POST', 'GET'])
def registration():
    print('1')
    if request.method == 'POST':
        form = Registrationform()
        print('2')
        if form.validate_on_submit():
            print('3')
            return redirect(url_for('index'))
    return render_template('registration.html', form=Registrationform())



@app.route('/login', methods=['POST', 'GET'])
def login():
    return render_template('login.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
