"""empty message

Revision ID: 2d983a8f6f31
Revises: 
Create Date: 2023-08-30 04:07:46.064162

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2d983a8f6f31'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gardens',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('location', sa.String(), nullable=False),
    sa.Column('size', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vegetables',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('veg_name', sa.String(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('ripeness', sa.String(), nullable=False),
    sa.Column('garden_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['garden_id'], ['gardens.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vegetables')
    op.drop_table('gardens')
    # ### end Alembic commands ###
