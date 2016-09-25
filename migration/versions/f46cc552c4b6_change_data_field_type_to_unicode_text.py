"""change data field type to unicode text

Revision ID: f46cc552c4b6
Revises: 45ab0ee0ba2f
Create Date: 2016-09-25 15:19:48.487678

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f46cc552c4b6'
down_revision = '45ab0ee0ba2f'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('images', 'data', existing_type=sa.UnicodeText(), nullable=False)


def downgrade():
    op.alter_column('images', 'data', existing_type=sa.BLOB(), nullable=False)
