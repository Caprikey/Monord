"""Make configs nullable and default to null

Revision ID: 091a10492adb
Revises: 12ba3a7fabd9
Create Date: 2018-06-19 11:40:16.186096

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '091a10492adb'
down_revision = '12ba3a7fabd9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('idx_guildconfig_region', table_name='guildconfig')
    op.drop_index('idx_gym_location', table_name='gym')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('idx_gym_location', 'gym', ['location'], unique=False)
    op.create_index('idx_guildconfig_region', 'guildconfig', ['region'], unique=False)
    # ### end Alembic commands ###