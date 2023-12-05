"""empty message

Revision ID: 6d9628653c10
Revises: 
Create Date: 2023-12-04 00:04:40.401122

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d9628653c10'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tb_user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=30), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('sex', sa.Boolean(), nullable=True),
    sa.Column('salary', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('tb_user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_tb_user_name'), ['name'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tb_user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_tb_user_name'))

    op.drop_table('tb_user')
    # ### end Alembic commands ###