from optimaint.db.database import Exam, Station, Train
from optimaint.db.config import SESSION, BASE, ENGINE

EXAMS = [
    Exam(name='C1', etype='C',
         req_mileage=0, req_days=0,
         tol_mileage=0, tol_days=0,
         duration='LONG'),
    Exam(name='C2', etype='C',
         req_mileage=0, req_days=0,
         tol_mileage=0, tol_days=0,
         duration='LONG')
]

for id in range(1, 9):
    EXAMS.append(
        Exam(name='S{}'.format(id), etype='S',
             req_mileage=0, req_days=0,
             tol_mileage=0, tol_days=0,
             duration='LONG')
    )
    EXAMS.append(
        Exam(name='M{}'.format(id), etype='M',
             req_mileage=0, req_days=0,
             tol_mileage=0, tol_days=0,
             duration='LONG')
    )

WC_STATIONS_MAP = {
    'BrtnUNCmd': ('Central Rivers (for WC)', 3),
    'PoldieCMD': ('Polmadie', 3),
    'Crewe CS': ('Crewe', 4),
    'Holyhead': ('Holyhead', 3),
}

XC_STATIONS_MAP = {
    'BartonUN': ('Central Rivers (for XC)', 5),
    'LongstCMD': ('Longsight', 4),
    'Elgh Dep': ('Eastleigh', 8),
    'Craig CS': ('Craigentinny', 6),
    'Tyne S.S.': ('Tyne Yard', 4),
    'CroftnDep': ('Crofton', 4),
    'LairaTRMD': ('Laira', 5),
    'Pznce TMD': ('Penzance', 2),
}

STATIONS = []

for station_id, station_data in WC_STATIONS_MAP.items():
    station_name, station_limit = station_data
    STATIONS.append(
        Station(uuid=station_id, name=station_name,
                company='WC', train_limit=station_limit))

for station_id, station_data in XC_STATIONS_MAP.items():
    station_name, station_limit = station_data
    STATIONS.append(
        Station(uuid=station_id, name=station_name,
                company='WC', train_limit=station_limit))

TRAINS = []

WC_TRAIN_UUIDS = [
    221101, 221102, 221103, 221104, 221105, 221106, 221107, 221108,
    221109, 221110, 221111, 221112, 221113, 221114, 221115, 221116,
    221117, 221118, 221142, 221143
]

XC_TRAIN_UUIDS_4 = [
    220001, 220011, 220021, 220031,
    220002, 220012, 220022, 220032,
    220003, 220013, 220023, 220033,
    220004, 220014, 220024, 220034,
    220005, 220015, 220025, 221136,
    220006, 220016, 220026, 221140,
    220007, 220017, 220027, 221141,
    220008, 220018, 220028, 221144,
    220009, 220019, 220029, 220010,
    220020, 220030
]

XC_TRAIN_UUIDS_5 = [
    221119, 221129,
    221120, 221130,
    221121, 221131,
    221122, 221132,
    221123, 221133,
    221124, 221134,
    221125, 221135,
    221126, 221137,
    221127, 221138,
    221128, 221139
]

for train_id in WC_TRAIN_UUIDS:
    TRAINS.append(Train(uuid=train_id, company='WC', no_cars=4))
for train_id in XC_TRAIN_UUIDS_4:
    TRAINS.append(Train(uuid=train_id, company='XC', no_cars=4))
for train_id in XC_TRAIN_UUIDS_5:
    TRAINS.append(Train(uuid=train_id, company='XC', no_cars=5))

if __name__ == '__main__':

    BASE.metadata.create_all(ENGINE)

    s = SESSION()

    print('TRAINS')
    for train in TRAINS:
        s.add(train)
    s.commit()

    print('EXAMS')
    for exam in EXAMS:
        s.add(exam)
    s.commit()

    print('STATIONS')
    for station in STATIONS:
        s.add(station)
    s.commit()

    print('FINISHED')
    s.commit()
