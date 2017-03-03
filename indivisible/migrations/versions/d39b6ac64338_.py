"""empty message

Revision ID: d39b6ac64338
Revises: 
Create Date: 2017-03-03 09:33:37.433492

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd39b6ac64338'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('committee',
    sa.Column('code', sa.String(length=10), nullable=False),
    sa.Column('congress', sa.Integer(), nullable=False),
    sa.Column('chamber', sa.String(length=10), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('committee_json', sa.String(length=1024), nullable=False),
    sa.Column('committee_hash', sa.String(length=32), nullable=False),
    sa.Column('last_updated', sa.DateTime(), server_default=sa.text(u'CURRENT_TIMESTAMP'), nullable=False),
    sa.PrimaryKeyConstraint('code')
    )
    op.create_table('congress',
    sa.Column('congress', sa.Integer(), nullable=False),
    sa.Column('last_updated', sa.DateTime(), server_default=sa.text(u'CURRENT_TIMESTAMP'), nullable=False),
    sa.PrimaryKeyConstraint('congress')
    )
    op.create_table('congressperson',
    sa.Column('id', sa.String(length=10), nullable=False),
    sa.Column('last_name', sa.String(length=30), nullable=False),
    sa.Column('first_name', sa.String(length=30), nullable=False),
    sa.Column('congress', sa.Integer(), nullable=False),
    sa.Column('chamber', sa.String(length=10), nullable=False),
    sa.Column('state', sa.String(length=2), nullable=False),
    sa.Column('district', sa.String(length=4), nullable=True),
    sa.Column('image', sa.String(length=200), nullable=True),
    sa.Column('member_json', sa.String(length=8192), nullable=False),
    sa.Column('member_hash', sa.String(length=32), nullable=False),
    sa.Column('last_updated', sa.DateTime(), server_default=sa.text(u'CURRENT_TIMESTAMP'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('congressperson')
    op.drop_table('congress')
    op.drop_table('committee')
    # ### end Alembic commands ###