"""adding location column to tasks table

Revision ID: 3115f24a7604
Revises: 38fe795129a0
Create Date: 2014-05-04 14:02:19.755081

"""

# revision identifiers, used by Alembic.
revision = '3115f24a7604'
down_revision = '38fe795129a0'

from alembic import op


def upgrade():
    # there is no way to tell alembic to add a geometry column the right way?
    op.execute(
        "SELECT AddGeometryColumn('tasks', 'location', 4326, 'POINT', 2)")
    # there is no way to tell alembic that we want a GiST type index?
    op.execute("CREATE INDEX idx_tasks_location ON tasks USING GIST(location)")


def downgrade():
    op.drop_index('idx_tasks_location', 'tasks')
    op.drop_column('tasks', 'location')
