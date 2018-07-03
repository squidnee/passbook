"""empty message

Revision ID: 9e89b2209417
Revises: 
Create Date: 2018-07-03 03:00:57.570445

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e89b2209417'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('wallet_record')
    op.drop_table('encrypted_document_record')
    op.drop_index('ix_record_email', table_name='record')
    op.drop_index('ix_record_username', table_name='record')
    op.drop_index('ix_record_website', table_name='record')
    op.drop_table('record')
    op.drop_table('category')
    op.drop_table('user')
    op.add_column('files', sa.Column('filename', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('files', 'filename')
    op.create_table('user',
    sa.Column('created_on', sa.DATETIME(), nullable=False),
    sa.Column('last_updated', sa.DATETIME(), nullable=True),
    sa.Column('last_accessed', sa.DATETIME(), nullable=True),
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=32), nullable=False),
    sa.Column('email', sa.VARCHAR(length=120), nullable=False),
    sa.Column('password_hash', sa.VARCHAR(length=128), nullable=True),
    sa.Column('is_manager', sa.BOOLEAN(), nullable=True),
    sa.Column('trusted_by', sa.VARCHAR(length=32), nullable=True),
    sa.Column('trusts', sa.VARCHAR(length=32), nullable=True),
    sa.CheckConstraint('is_manager IN (0, 1)'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('trusted_by'),
    sa.UniqueConstraint('trusts'),
    sa.UniqueConstraint('username')
    )
    op.create_table('category',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('record',
    sa.Column('created_on', sa.DATETIME(), nullable=False),
    sa.Column('last_updated', sa.DATETIME(), nullable=True),
    sa.Column('last_accessed', sa.DATETIME(), nullable=True),
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=128), nullable=False),
    sa.Column('owner', sa.VARCHAR(length=32), nullable=False),
    sa.Column('category', sa.INTEGER(), nullable=False),
    sa.Column('website', sa.VARCHAR(length=128), nullable=False),
    sa.Column('username', sa.VARCHAR(length=64), nullable=True),
    sa.Column('password', sa.VARCHAR(length=128), nullable=True),
    sa.Column('password_hash', sa.VARCHAR(length=128), nullable=True),
    sa.Column('description', sa.VARCHAR(length=200), nullable=True),
    sa.Column('notes', sa.VARCHAR(length=500), nullable=True),
    sa.Column('email', sa.VARCHAR(length=120), nullable=True),
    sa.Column('expiration_date', sa.DATE(), nullable=True),
    sa.Column('version', sa.INTEGER(), nullable=True),
    sa.Column('files', sa.BLOB(), nullable=True),
    sa.Column('starred', sa.BOOLEAN(), nullable=True),
    sa.Column('reprompt', sa.BOOLEAN(), nullable=True),
    sa.CheckConstraint('reprompt IN (0, 1)'),
    sa.CheckConstraint('starred IN (0, 1)'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index('ix_record_website', 'record', ['website'], unique=False)
    op.create_index('ix_record_username', 'record', ['username'], unique=False)
    op.create_index('ix_record_email', 'record', ['email'], unique=False)
    op.create_table('encrypted_document_record',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('document', sa.BLOB(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('wallet_record',
    sa.Column('created_on', sa.DATETIME(), nullable=False),
    sa.Column('last_updated', sa.DATETIME(), nullable=True),
    sa.Column('last_accessed', sa.DATETIME(), nullable=True),
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('card_name', sa.VARCHAR(length=128), nullable=True),
    sa.Column('card_type', sa.VARCHAR(length=128), nullable=True),
    sa.Column('card_number', sa.INTEGER(), nullable=False),
    sa.Column('name_on_card', sa.VARCHAR(length=128), nullable=False),
    sa.Column('expiration_date', sa.DATE(), nullable=False),
    sa.Column('secret_code', sa.INTEGER(), nullable=False),
    sa.Column('zip_code', sa.INTEGER(), nullable=True),
    sa.Column('description', sa.VARCHAR(length=200), nullable=True),
    sa.Column('notes', sa.VARCHAR(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###