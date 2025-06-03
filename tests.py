import pytest
from app import app, db, Books

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # use in-memory DB
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'<html' in response.data or b'<!DOCTYPE html' in response.data

def test_book_route(client):
    with app.app_context():
        book = Books(title="Flask Testing", category="Tech")
        db.session.add(book)
        db.session.commit()
        book_id = book.id

    response = client.get(f'/book?book_id={book_id}')
    assert response.status_code == 200
    assert b'Flask Testing' in response.data

