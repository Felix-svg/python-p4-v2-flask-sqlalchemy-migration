"""rename department

Revision ID: f973d0f5c1ee
Revises: baac9a264b93
Create Date: 2024-04-02 10:16:33.477351

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f973d0f5c1ee"
down_revision = "baac9a264b93"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table("department", "departments")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table("departments", "department")
    # ### end Alembic commands ###
