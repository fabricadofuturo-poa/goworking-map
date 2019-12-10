"""empty message

Revision ID: fb9a770a745b
Revises: 97b6faa5a92c
Create Date: 2019-12-10 18:50:21.413675

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb9a770a745b'
down_revision = '97b6faa5a92c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('espaco_v1',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('timestamp', sa.TIMESTAMP(), nullable=True),
    sa.Column('numero', sa.String(length=2), nullable=True),
    sa.Column('ordem', sa.Integer(), nullable=True),
    sa.Column('desc', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_index(op.f('ix_espaco_v1_timestamp'), 'espaco_v1', ['timestamp'], unique=False)
    op.add_column('mesa_v1', sa.Column('id_espaco', sa.String(length=36), nullable=True))
    op.create_foreign_key(None, 'mesa_v1', 'espaco_v1', ['id_espaco'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'mesa_v1', type_='foreignkey')
    op.drop_column('mesa_v1', 'id_espaco')
    op.drop_index(op.f('ix_espaco_v1_timestamp'), table_name='espaco_v1')
    op.drop_table('espaco_v1')
    # ### end Alembic commands ###
