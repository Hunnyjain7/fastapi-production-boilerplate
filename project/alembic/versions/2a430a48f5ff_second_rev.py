"""second rev

Revision ID: 2a430a48f5ff
Revises: a104c3b16287
Create Date: 2022-10-24 13:38:05.328945

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a430a48f5ff'
down_revision = 'a104c3b16287'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usr_user', sa.Column('user_three_id', sa.CHAR(length=38), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('usr_user', 'user_three_id')
    # ### end Alembic commands ###
