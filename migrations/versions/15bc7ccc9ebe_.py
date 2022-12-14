"""empty message

Revision ID: 15bc7ccc9ebe
Revises: 
Create Date: 2022-09-14 16:30:07.100464

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15bc7ccc9ebe'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=True),
    sa.Column('work', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
