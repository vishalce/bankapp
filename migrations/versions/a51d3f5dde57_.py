"""empty message

Revision ID: a51d3f5dde57
Revises: d0c379fb04b2
Create Date: 2019-11-08 15:45:17.355134

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a51d3f5dde57'
down_revision = 'd0c379fb04b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_banks_name'), 'banks', ['name'], unique=False)
    op.create_index(op.f('ix_branches_city'), 'branches', ['city'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_branches_city'), table_name='branches')
    op.drop_index(op.f('ix_banks_name'), table_name='banks')
    # ### end Alembic commands ###
