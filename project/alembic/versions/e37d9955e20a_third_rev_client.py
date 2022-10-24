"""third rev client

Revision ID: e37d9955e20a
Revises: 2a430a48f5ff
Create Date: 2022-10-24 13:41:58.020844

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e37d9955e20a'
down_revision = '2a430a48f5ff'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cli_client',
    sa.Column('client_id', sa.CHAR(length=38), nullable=True),
    sa.Column('association_id', sa.CHAR(length=38), nullable=True),
    sa.Column('association_type_term', sa.VARCHAR(length=39), nullable=True),
    sa.Column('status_term', sa.VARCHAR(length=39), nullable=True),
    sa.Column('display_name', sa.VARCHAR(length=61), nullable=True),
    sa.Column('created_on', sa.DATETIME(), nullable=True),
    sa.Column('created_by', sa.CHAR(length=39), nullable=True),
    sa.Column('updated_on', sa.DATETIME(), nullable=True),
    sa.Column('updated_by', sa.CHAR(length=39), nullable=True),
    sa.Column('is_active', sa.String(length=1), nullable=True),
    sa.Column('is_delete', sa.String(length=1), nullable=True),
    sa.Column('update_log', sa.TIMESTAMP(), nullable=True),
    sa.Column('seq_no', sa.INTEGER(), nullable=False),
    sa.Column('user_type_term', sa.VARCHAR(length=39), nullable=True),
    sa.PrimaryKeyConstraint('seq_no')
    )
    op.create_index(op.f('ix_cli_client_seq_no'), 'cli_client', ['seq_no'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_cli_client_seq_no'), table_name='cli_client')
    op.drop_table('cli_client')
    # ### end Alembic commands ###