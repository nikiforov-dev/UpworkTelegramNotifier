"""create jobs table

Revision ID: 18609f883b74
Revises: 
Create Date: 2023-03-04 01:15:45.083846

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18609f883b74'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'jobs',
        sa.Column('id', sa.Integer, primary_key=True, nullable=False, autoincrement=True),
        sa.Column('hash', sa.String, unique=True, nullable=False),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('link', sa.String, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False, server_default=sa.func.current_timestamp()),
    )


def downgrade() -> None:
    op.drop_table('jobs')
