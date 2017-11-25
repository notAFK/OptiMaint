import os

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DB_ENV = "prod"  # can be test
if DB_ENV == "local":
    _db = ":memory:"
else:
    _db = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "database.db"))

ENGINE = create_engine("sqlite:///{}".format(_db), echo=True)
BASE = declarative_base(metadata=MetaData())
SESSION = sessionmaker(bind=ENGINE)
