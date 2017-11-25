from contextlib import contextmanager

from optimaint.db.config import BASE, SESSION
from sqlalchemy import Column, Integer, String, Date, ForeignKey


class Exam(BASE):
    __tablename__ = 'exams'

    # C1, C2, S1-8, M1-8
    name = Column(String(2), primary_key=True)

    # C, S, M
    etype = Column(String(1))

    # Point when train should come for exam
    req_mileage = Column(Integer)
    req_days = Column(Integer)

    # Tolerance for when train should come
    tol_mileage = Column(Integer)
    tol_days = Column(Integer)


class Diagram(BASE):
    __tablename__ = 'diagrams'

    # Unique ID created using a hash function on (ID, Days, Range Dates)
    uuid = Column(Integer, primary_key=True)

    # ID is of form XXX digits (eg: 501)
    id = Column(Integer)

    company = Column(String)
    no_cars = Column(Integer)

    period_start = Column(Date)
    period_end = Column(Date)
    period_days = Column(String)

    start_station = Column(String, ForeignKey('stations.uuid'))
    end_station = Column(String, ForeignKey('stations.uuid'))


class Station(BASE):
    __tablename__ = 'stations'

    uuid = Column(Integer, primary_key=True)
    name = Column(String)
    company = Column(String)
    train_limit = Column(Integer)


class Train(BASE):
    __tablename__ = 'trains'

    uuid = Column(Integer, primary_key=True)
    company = Column(String)
    no_cars = Column(Integer)


@contextmanager
def session():
    s = SESSION()
    try:
        yield s
        s.commit()
    except Exception as e:
        print('EXCEPTION:')
        print(e)
    finally:
        s.close()
