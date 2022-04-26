"""Changing column names

Revision ID: 4cf7a741b4ed
Revises: 09bc879baf5a
Create Date: 2022-04-26 11:26:19.139442

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4cf7a741b4ed'
down_revision = '09bc879baf5a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('personal', sa.Column('nome', sa.String(), nullable=False))
    op.add_column('personal', sa.Column('senha_hash', sa.String(), nullable=False))
    op.drop_column('personal', 'name')
    op.drop_column('personal', 'password_hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('personal', sa.Column('password_hash', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('personal', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('personal', 'senha_hash')
    op.drop_column('personal', 'nome')
    # ### end Alembic commands ###