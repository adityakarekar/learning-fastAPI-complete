"""add a new cloumn called content in posts table

Revision ID: f6056d336d41
Revises: 2860b7de518d
Create Date: 2025-08-12 16:58:05.430506

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f6056d336d41'
down_revision: Union[str, Sequence[str], None] = '2860b7de518d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts",sa.Column("content",sa.String(),nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts", "content")
    pass
