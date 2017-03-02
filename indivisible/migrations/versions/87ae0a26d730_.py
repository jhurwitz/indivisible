"""empty message

Revision ID: 87ae0a26d730
Revises: d39b6ac64338
Create Date: 2017-03-03 09:39:05.511980

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87ae0a26d730'
down_revision = 'd39b6ac64338'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'congressperson', 'congress', ['congress'], ['congress'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'congressperson', type_='foreignkey')
    # ### end Alembic commands ###
