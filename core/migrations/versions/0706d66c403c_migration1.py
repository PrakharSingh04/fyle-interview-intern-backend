"""migration1

Revision ID: 0706d66c403c
Revises: 52a401750a76
Create Date: 2024-04-26 02:44:54.098489

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0706d66c403c'
down_revision = '52a401750a76'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('assignments', schema=None) as batch_op:
        batch_op.alter_column('state',
               existing_type=sa.VARCHAR(length=9),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('assignments', schema=None) as batch_op:
        batch_op.alter_column('state',
               existing_type=sa.VARCHAR(length=9),
               nullable=True)

    # ### end Alembic commands ###
