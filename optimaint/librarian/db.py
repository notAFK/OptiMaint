import os

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Date


_db = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "database.db"))

ENGINE = create_engine("sqlite:///{}".format(_db), echo=True)
BASE = declarative_base(metadata=MetaData())
SESSION = sessionmaker(bind=ENGINE)


class Arrival(BASE):
    __tablename__ = 'arrivals'
    # Diagram	H/C	From	"ArrTime"	Unit	Exam	Comments

    station_id = Column(String)

    uuid = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    diagram = Column(String)
    hc = Column(String)
    from_station = Column(String)
    arrival_time = Column(String)
    unit = Column(Integer)
    exam = Column(String)
    date = Column(Date)


class Departure(BASE):
    __tablename__ = 'departures'
    # Diagram	H/C	"Start Time"	"Finish Depot"	Time	"Diag Miles"	Unit	Comments	On Time?

    station_id = Column(String)

    uuid = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    diagram = Column(String)
    hc = Column(String)
    finish_depot = Column(String)
    time = Column(String)
    miles = Column(Float)
    unit = Column(Integer)
    date = Column(Date)


BASE.metadata.create_all(ENGINE)
s = SESSION()
s.commit()
