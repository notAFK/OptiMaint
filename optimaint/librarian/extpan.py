from optimaint.db.database import AnnTrain
from optimaint.db.database import session
import xlrd

COL_MAP = {
    'uuid': 15,
    'next_service': 17,
    'last_service_miles': 21,
    'last_service_days': 22,
    'next_core': 29,
    'last_core_miles': 30,
    'last_core_days': 31,
    'next_mv': 38,
    'last_mv_miles': 39,
    'last_mv_days': 40
}

NO_TRAINS = 79


def extract_planner(file_path):
    book = xlrd.open_workbook(file_path)
    sheet = book.sheet_by_name('220')

    for rx in range(1, NO_TRAINS):
        vals = [sheet.row(rx)[i].value for i in COL_MAP.values()]

        uuid, next_service, last_service_miles, last_service_days, next_core, last_core_miles, last_core_days, next_mv, last_mv_miles, last_mv_days = vals
        uuid = int(uuid)

        with session() as s:
            s.add(AnnTrain(uuid=uuid, next_service=next_service,
                  last_service_miles=last_service_miles,
                  last_service_days=last_service_days, next_core=next_core,
                  last_core_miles=last_core_miles,
                  last_core_days=last_core_days,
                  next_mv=next_mv, last_mv_miles=last_mv_miles,
                  last_mv_days=last_mv_days))


file_path = 'history/2017/july/Exam Plan 17 07 17.xlsm'
extract_planner(file_path)
