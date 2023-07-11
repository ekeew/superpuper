"""Add users

Revision ID: 9db6067ff06d
Revises: 
Create Date: 2023-07-11 11:48:26.045371

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9db6067ff06d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'users',
        sa.Column('tg_id', sa.BIGINT(), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint('tg_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###