"""Del completion_rate field

Revision ID: 7dcbabb3915e
Revises: 1b6743b2e629
Create Date: 2023-07-02 17:00:13.543380

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7dcbabb3915e'
down_revision = '1b6743b2e629'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('charityproject', 'completion_rate')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('charityproject', sa.Column('completion_rate', sa.DATETIME(), nullable=True))
    # ### end Alembic commands ###
