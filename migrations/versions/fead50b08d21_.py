"""empty message

Revision ID: fead50b08d21
Revises: 
Create Date: 2019-12-09 16:11:49.548100

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fead50b08d21'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('empresa_v1',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('timestamp', sa.TIMESTAMP(), nullable=True),
    sa.Column('nome', sa.String(length=255), nullable=False),
    sa.Column('cnpj', sa.String(length=14), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_index(op.f('ix_empresa_v1_timestamp'), 'empresa_v1', ['timestamp'], unique=False)
    op.create_table('mesa_v1',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('timestamp', sa.TIMESTAMP(), nullable=True),
    sa.Column('numero', sa.String(length=2), nullable=True),
    sa.Column('ordem', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_index(op.f('ix_mesa_v1_timestamp'), 'mesa_v1', ['timestamp'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('timestamp', sa.TIMESTAMP(), nullable=True),
    sa.Column('nome', sa.String(length=255), nullable=False),
    sa.Column('pronome', sa.String(length=2), nullable=True),
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('last_login', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_user_timestamp'), 'user', ['timestamp'], unique=False)
    op.create_table('cadeira_v1',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('timestamp', sa.TIMESTAMP(), nullable=True),
    sa.Column('numero', sa.String(length=4), nullable=True),
    sa.Column('ordem', sa.Integer(), nullable=True),
    sa.Column('id_mesa', sa.String(length=36), nullable=True),
    sa.ForeignKeyConstraint(['id_mesa'], ['mesa_v1.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_index(op.f('ix_cadeira_v1_timestamp'), 'cadeira_v1', ['timestamp'], unique=False)
    op.create_table('habitante_v1',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('timestamp', sa.TIMESTAMP(), nullable=True),
    sa.Column('nome', sa.String(length=255), nullable=False),
    sa.Column('cpf', sa.String(length=11), nullable=True),
    sa.Column('data_entrada', sa.DateTime(), nullable=True),
    sa.Column('data_saida', sa.DateTime(), nullable=True),
    sa.Column('data_renovacao', sa.DateTime(), nullable=True),
    sa.Column('id_empresa', sa.String(length=36), nullable=True),
    sa.Column('id_cadeira', sa.String(length=36), nullable=True),
    sa.Column('desc', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['id_cadeira'], ['cadeira_v1.id'], ),
    sa.ForeignKeyConstraint(['id_empresa'], ['empresa_v1.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_index(op.f('ix_habitante_v1_timestamp'), 'habitante_v1', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_habitante_v1_timestamp'), table_name='habitante_v1')
    op.drop_table('habitante_v1')
    op.drop_index(op.f('ix_cadeira_v1_timestamp'), table_name='cadeira_v1')
    op.drop_table('cadeira_v1')
    op.drop_index(op.f('ix_user_timestamp'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_mesa_v1_timestamp'), table_name='mesa_v1')
    op.drop_table('mesa_v1')
    op.drop_index(op.f('ix_empresa_v1_timestamp'), table_name='empresa_v1')
    op.drop_table('empresa_v1')
    # ### end Alembic commands ###
