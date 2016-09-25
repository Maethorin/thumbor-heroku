"""create image table

Revision ID: 8c2eabecb5aa
Revises: 
Create Date: 2016-09-24 15:23:22.663732

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c2eabecb5aa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'images',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('path', sa.String(), unique=True, nullable=False),
        sa.Column('data', sa.Text(), nullable=False),
        sa.Column('detector', sa.Text(), nullable=True),
        sa.Column('crypto', sa.Text(), nullable=True)
    )


def downgrade():
    op.drop_table('images')
