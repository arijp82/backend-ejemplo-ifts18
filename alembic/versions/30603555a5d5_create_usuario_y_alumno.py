"""create usuario y alumno

Revision ID: 30603555a5d5
Revises: 
Create Date: 2025-04-08 19:44:24.291793

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '30603555a5d5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_usuario_email'), 'usuario', ['email'], unique=True)
    op.create_index(op.f('ix_usuario_id'), 'usuario', ['id'], unique=False)
    op.create_table('alumno',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('carrera', sa.String(), nullable=True),
    sa.Column('usuario_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_alumno_id'), 'alumno', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_alumno_id'), table_name='alumno')
    op.drop_table('alumno')
    op.drop_index(op.f('ix_usuario_id'), table_name='usuario')
    op.drop_index(op.f('ix_usuario_email'), table_name='usuario')
    op.drop_table('usuario')
    # ### end Alembic commands ###
