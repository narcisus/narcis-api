from sqlalchemy import create_engine

from narcis_api import config, models

engine = create_engine(config.db)
models.Base.metadata.create_all(engine)
