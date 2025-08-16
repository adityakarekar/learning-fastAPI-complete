"""add foreign key to post table

Revision ID: 0014802e9d61
Revises: ab69360c67ff
Create Date: 2025-08-12 17:22:47.093232

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0014802e9d61'
down_revision: Union[str, Sequence[str], None] = 'ab69360c67ff'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts",sa.Column("owner_id",sa.Integer(),nullable=False))
    op.create_foreign_key("fk_posts_users", "posts", "users", ["owner_id"], ["id"],ondelete="CASCADE")
    # This creates a foreign key constraint on the posts table, linking owner_id to the id column in the users table.
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint("fk_posts_users", "posts", type_="foreignkey")
    op.drop_column("posts", "owner_id")
    pass
