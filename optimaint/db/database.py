from optimaint.db.config import BASE
from sqlalchemy import Column, Integer, String, Date, ForeignKey


class Exam(BASE):
    __tablename__ = 'exams'

    # C1, C2, S1-8, M1-8
    name = Column(String(2), primary_key=True, unique=True)

    # C, S, M
    etype = Column(String(1))

    # Point when train should come for exam
    req_mileage = Column(Integer)
    req_days = Column(Integer)

    # Tolerance for when train should come
    tol_mileage = Column(Integer)
    tol_days = Column(Integer)

    # Short or long duration
    duration = Column(String)


class Diagram(BASE):
    __tablename__ = 'diagrams'

    # Unique ID created using a hash function on (ID, Days, Range Dates)
    uuid = Column(Integer, primary_key=True, unique=True)

    # ID is of form XXX digits (eg: 501)
    id = Column(Integer)

    total_mileage = Column(Integer)

    company = Column(String)
    no_cars = Column(Integer)

    period_start = Column(Date)
    period_end = Column(Date)
    period_days = Column(String)

    schedule_uuid = Column(Integer, ForeignKey('schedules.uuid'))


class Station(BASE):
    __tablename__ = 'stations'

    uuid = Column(String, primary_key=True, unique=True)
    name = Column(String)
    company = Column(String)
    train_limit = Column(Integer)


class Train(BASE):
    __tablename__ = 'trains'

    uuid = Column(Integer, primary_key=True, unique=True)
    company = Column(String)
    no_cars = Column(Integer)


class Assignment(BASE):
    __tablename__ = 'assignments'

    uuid = Column(Integer, primary_key=True, unique=True)
    train_uuid = Column(Integer, ForeignKey('trains.uuid'))
    diagram_uuid = Column(Integer, ForeignKey('diagrams.uuid'))


class ExamEntry(BASE):
    __tablename__ = 'exam_logs'

    uuid = Column(Integer, primary_key=True, unique=True)
    train_uuid = Column(Integer, ForeignKey('trains.uuid'))
    exam_name = Column(Integer, ForeignKey('exams.name'))
    date = Column(Date)


class Schedule(BASE):
    __tablename__ = 'schedules'

    uuid = Column(Integer, primary_key=True, unique=True)

    start_station_uuid = Column(Integer, ForeignKey('stations.uuid'))
    end_station_uuid = Column(Integer, ForeignKey('stations.uuid'))

    start_time = Column(Date)
    end_time = Column(Date)


# @contextmanager
# def session():
#     s = SESSION()
#     try:
#         yield s
#         s.commit()
#     except Exception as e:
#         print('EXCEPTION:')
#         print(e)
#     finally:
#         s.close()
