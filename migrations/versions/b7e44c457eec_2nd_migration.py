"""2nd migration

Revision ID: b7e44c457eec
Revises: 
Create Date: 2022-09-27 17:17:47.785161

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7e44c457eec'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('authors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_authors_name'), 'authors', ['name'], unique=True)
    op.create_table('association',
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['authors.id'], ),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], ),
    sa.PrimaryKeyConstraint('book_id', 'author_id')
    )
    op.create_index(op.f('ix_books_title'), 'books', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_books_title'), table_name='books')
    op.drop_table('association')
    op.drop_index(op.f('ix_authors_name'), table_name='authors')
    op.drop_table('authors')
    # ### end Alembic commands ###