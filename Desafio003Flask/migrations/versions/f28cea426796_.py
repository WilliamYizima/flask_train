"""empty message

Revision ID: f28cea426796
Revises: fe1946c1ea9a
Create Date: 2020-07-19 04:23:42.766633

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f28cea426796'
down_revision = 'fe1946c1ea9a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tb_comment', sa.Column('fg_post', sa.Integer(), nullable=False))
    op.drop_constraint('tb_comment_fg_comment_fkey', 'tb_comment', type_='foreignkey')
    op.create_foreign_key(None, 'tb_comment', 'tb_post', ['fg_post'], ['id_post'])
    op.drop_column('tb_comment', 'fg_comment')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tb_comment', sa.Column('fg_comment', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'tb_comment', type_='foreignkey')
    op.create_foreign_key('tb_comment_fg_comment_fkey', 'tb_comment', 'tb_post', ['fg_comment'], ['id_post'])
    op.drop_column('tb_comment', 'fg_post')
    # ### end Alembic commands ###
