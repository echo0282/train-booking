"""empty message

Revision ID: 1d5c640215b0
Revises: None
Create Date: 2015-09-18 23:00:19.158763

"""

# revision identifiers, used by Alembic.
revision = '1d5c640215b0'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('trains',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('train_id', sa.String(), nullable=False),
    sa.Column('fromCity', sa.String(), nullable=False),
    sa.Column('toCity', sa.String(), nullable=False),
    sa.Column('size', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('trains')
    ### end Alembic commands ###
