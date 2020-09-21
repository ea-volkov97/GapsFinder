import sqlalchemy as sa

# TODO: модель представляения данных в БД
surface = sa.Table(
    "surface",
    sa.Column('id', sa.Integer, primary_key=True),
)
