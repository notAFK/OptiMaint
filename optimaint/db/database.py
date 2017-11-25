from contextlib import contextmanager

from optimaint.db.config import BASE, SESSION, ENGINE
from sqlalchemy import Column, Integer, String, Date

class Exam(BASE):
    __tablename__ = 'exams'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    exam_type = Column(String)
    mile_range = Column(Integer, nullable=True)
    day_ramge = Column(Integer, nullable=True)
    mile_tolerance = Column(Integer, nullable=True)
    day_tolerance = Column(Integer, nullable=True)


class Diagram(BASE):
    __tablename__ = 'diagrams'

    id = Column(Integer, primary_key=True)
    hash = Column(String)
    company = Column(String)
    start_station = Column(String)
    end_station = Column(String)
    nr_cars = Column(Integer)
    period_start = Column(Date)
    period_end = Column(Date)


class Station(object):
    __tablename__ = 'stations'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    company = Column(String)
    train_limit = Column(Integer)


class Train(object):
    __tablename__ = 'trains'

    id = Column(Integer, primary_key=True)
    company = Column(String)
    no_cars = Column(Integer)
    miles_since_core = Column(Integer)
    last_core = Column(Integer)
    days_since_service = Column(Integer)
    last_service = Column(Integer)
    miles_since_mv = Column(Integer)
    days_since_mv = Column(Integer)


@contextmanager
def session():
    s = SESSION()
    try:
        yield s
        s.commit()
    except Exception as e:
        print(e)
    finally:
        s.close()

def create_schema():
    BASE.metadata.create_all(ENGINE)


if __name__ == "__main__":
    create_schema()