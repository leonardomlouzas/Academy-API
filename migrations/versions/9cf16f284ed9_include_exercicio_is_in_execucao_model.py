"""Include exercicio_is in execucao model

Revision ID: 9cf16f284ed9
Revises: ecd6b7e95ff2
Create Date: 2022-05-03 13:06:16.959642

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9cf16f284ed9'
down_revision = 'ecd6b7e95ff2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('execucao', sa.Column('exercicio_id', sa.Integer(), nullable=False))
    op.create_unique_constraint(None, 'execucao', ['exercicio_id'])
    op.create_foreign_key(None, 'execucao', 'exercicio', ['exercicio_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'execucao', type_='foreignkey')
    op.drop_constraint(None, 'execucao', type_='unique')
    op.drop_column('execucao', 'exercicio_id')
    # ### end Alembic commands ###
