"""empty message

Revision ID: ece75bc923a1
Revises: None
Create Date: 2018-07-03 11:20:25.047626

"""

# revision identifiers, used by Alembic.
revision = 'ece75bc923a1'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('baskets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('baskets_items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('baskets', sa.Integer(), nullable=True),
    sa.Column('items', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['baskets'], ['baskets.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['items'], ['items.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=250), nullable=False),
    sa.Column('last_name', sa.String(length=250), nullable=False),
    sa.Column('is_loyal', sa.Boolean(), nullable=True),
    sa.Column('creation_date', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('basket_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['basket_id'], ['baskets.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('baskets_items')
    op.drop_table('items')
    op.drop_table('baskets')
    # ### end Alembic commands ###
