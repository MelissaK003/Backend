"""Change field type from Integer to String

Revision ID: ff45c93507e7
Revises: f2aa322f84ec
Create Date: 2025-03-05 23:13:04.247381

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff45c93507e7'
down_revision = 'f2aa322f84ec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('work_order', schema=None) as batch_op:
        batch_op.alter_column('number_plate',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=64),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('work_order', schema=None) as batch_op:
        batch_op.alter_column('number_plate',
               existing_type=sa.String(length=64),
               type_=sa.INTEGER(),
               existing_nullable=True)

    # ### end Alembic commands ###
