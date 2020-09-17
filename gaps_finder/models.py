import sqlalchemy as sa
from sqlalchemy.types import JSON

metadata = sa.MetaData()

__all__ = ['surface', 'get_engine']

surface = sa.Table(
    "surface", metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column("xyz_grid", sa.PickleType, nullable=False),
    sa.Column("plane_cords", sa.JSON, default=[], nullable=False),
    sa.Column("dots_per_length", sa.Integer, nullable=False),
    sa.Column("dots_per_width", sa.Integer, nullable=False),
    sa.Column("plane_cords_count", sa.Integer, nullable=False),
    sa.Column("meta", JSON, default={})
)


def get_engine(user=None, password=None, host=None, port=None, db_name=None):
    db_url = ''.format(
        user=user,
        password=password,
        host=host,
        db_name=db_name,
        port=str(port)
    )

    return sa.create_engine(db_url)


def create_tables(engine):
    metadata.create_all(engine, checkfirst=True)