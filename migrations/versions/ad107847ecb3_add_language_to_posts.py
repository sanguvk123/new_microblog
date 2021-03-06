"""add language to posts

Revision ID: ad107847ecb3
Revises: 7d4e9517c8b5
Create Date: 2021-08-06 02:26:41.387583

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad107847ecb3'
down_revision = '7d4e9517c8b5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_message_timestamp', table_name='message')
    op.drop_table('message')
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    op.drop_column('user', 'last_message_read_time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('last_message_read_time', sa.DATETIME(), nullable=True))
    op.drop_column('post', 'language')
    op.create_table('message',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('sender_id', sa.INTEGER(), nullable=True),
    sa.Column('recipient_id', sa.INTEGER(), nullable=True),
    sa.Column('body', sa.VARCHAR(length=140), nullable=True),
    sa.Column('timestamp', sa.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['recipient_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['sender_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_message_timestamp', 'message', ['timestamp'], unique=False)
    # ### end Alembic commands ###
