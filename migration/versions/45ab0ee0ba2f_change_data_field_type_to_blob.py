"""change data field type to blob

Revision ID: 45ab0ee0ba2f
Revises: 8c2eabecb5aa
Create Date: 2016-09-25 14:10:54.044318

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45ab0ee0ba2f'
down_revision = '8c2eabecb5aa'
branch_labels = None
depends_on = None


def upgrade():
    op.create_unique_constraint(None, 'images', ['path'])
    op.alter_column('images', 'data', existing_type=sa.BLOB(), nullable=False)


def downgrade():
    op.alter_column('images', 'data', existing_type=sa.Text(), nullable=False)
    op.drop_constraint(None, 'images', type_='unique')
