"""baseline

Revision ID: 12ba3a7fabd9
Revises: 
Create Date: 2018-06-19 11:39:04.845761

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2

# revision identifiers, used by Alembic.
revision = '12ba3a7fabd9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.Column('start_time', sa.DateTime(), nullable=True),
    sa.Column('end_time', sa.DateTime(), nullable=True),
    sa.Column('done', sa.Boolean(), nullable=True),
    sa.Column('cancelled', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('guildconfig',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('guild_id', sa.BigInteger(), nullable=True),
    sa.Column('channel_id', sa.BigInteger(), nullable=True),
    sa.Column('mirror', sa.Boolean(), nullable=True),
    sa.Column('region', geoalchemy2.types.Geometry(geometry_type='POLYGON', srid=4326), nullable=True),
    sa.Column('timezone', sa.String(), nullable=True),
    sa.Column('subscriptions', sa.Boolean(), nullable=True),
    sa.Column('delete_after_despawn', sa.Integer(), nullable=True),
    sa.Column('emoji_going', sa.String(), nullable=True),
    sa.Column('emoji_add_person', sa.String(), nullable=True),
    sa.Column('emoji_remove_person', sa.String(), nullable=True),
    sa.Column('emoji_add_time', sa.String(), nullable=True),
    sa.Column('emoji_remove_time', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('gym',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('location', geoalchemy2.types.Geometry(geometry_type='POINT', srid=4326), nullable=True),
    sa.Column('ex', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('party',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('creator_user_id', sa.BigInteger(), nullable=True),
    sa.Column('user_id', sa.BigInteger(), nullable=True),
    sa.Column('guild_id', sa.BigInteger(), nullable=True),
    sa.Column('extra', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('creator_user_id', 'user_id', name='_creator_user_id_user_id_uc')
    )
    op.create_table('pokemon',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('raid_level', sa.Integer(), nullable=True),
    sa.Column('ex', sa.Boolean(), nullable=True),
    sa.Column('types', sa.Integer(), nullable=True),
    sa.Column('perfect_cp', sa.Integer(), nullable=True),
    sa.Column('perfect_cp_boosted', sa.Integer(), nullable=True),
    sa.Column('availability_rules', sa.String(), nullable=True),
    sa.Column('shiny', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pokestop',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('eventgoing',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.BigInteger(), nullable=True),
    sa.Column('guild_id', sa.BigInteger(), nullable=True),
    sa.Column('extra', sa.Integer(), nullable=True),
    sa.Column('event_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('gymalias',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('gym_id', sa.Integer(), nullable=True),
    sa.Column('guild_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['gym_id'], ['gym.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('raid',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pokemon_id', sa.Integer(), nullable=True),
    sa.Column('gym_id', sa.Integer(), nullable=True),
    sa.Column('despawn_time', sa.DateTime(), nullable=True),
    sa.Column('start_time', sa.DateTime(), nullable=True),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.Column('ex', sa.Boolean(), nullable=True),
    sa.Column('hatched', sa.Boolean(), nullable=True),
    sa.Column('despawned', sa.Boolean(), nullable=True),
    sa.Column('cancelled', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['gym_id'], ['gym.id'], ),
    sa.ForeignKeyConstraint(['pokemon_id'], ['pokemon.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('embed',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('channel_id', sa.BigInteger(), nullable=True),
    sa.Column('message_id', sa.BigInteger(), nullable=True),
    sa.Column('raid_id', sa.Integer(), nullable=True),
    sa.Column('embed_type', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['raid_id'], ['raid.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('raidgoing',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.BigInteger(), nullable=True),
    sa.Column('guild_id', sa.BigInteger(), nullable=True),
    sa.Column('extra', sa.Integer(), nullable=True),
    sa.Column('raid_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['raid_id'], ['raid.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('raid_id', 'user_id', name='_raid_id_user_uc')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('raidgoing')
    op.drop_table('embed')
    op.drop_table('raid')
    op.drop_table('gymalias')
    op.drop_table('eventgoing')
    op.drop_table('pokestop')
    op.drop_table('pokemon')
    op.drop_table('party')
    op.drop_table('gym')
    op.drop_table('guildconfig')
    op.drop_table('event')
    # ### end Alembic commands ###
