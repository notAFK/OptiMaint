import xlrd
# from optimaint.librarian.db import Arrival, Departure, SESSION


ABRV = ['EC', 'XW', 'MA', 'CZ', 'BK', 'LA', 'PZ', 'EH']
# s = SESSION()


def parse_sheet(sh):
    # print('  ', sh.name, sh.nrows, sh.ncols)
    print(sh.name)
    for rx in range(sh.nrows):
        rval = sh.cell_value(rowx=rx, colx=8)
        if rval in ABRV:
            parse_location(sh, rx, 0)


def parse_location(sh, x, y):
    id = sh.cell_value(rowx=x, colx=8)
    # name = sh.cell_value(rowx=x, colx=0).split('(')[0]

    # FUCK THIS FUCKING FORMAT
    # date = sh.cell_value(rowx=x+1, colx=3)

    # print(id, name)

    # Arrivals
    # print('ARIV')
    for nx in range(x+3, x+30):
        if sh.cell_type(nx, 0) not in (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK):
            row = sh.row(nx)[:7]
            diag, hc, frm, artime, unit, exam, comment = row

            if str(diag.value).strip() == '' and unit.value == '':
                break

            if str(diag.value).strip() == '' or unit.value == '':
                continue

            if diag.value == 'Diagram' or diag.value == 'Signed (Depot representative) :':
                break

            if diag.value == 'VSTP':
                continue

            if unit.ctype is xlrd.XL_CELL_TEXT:
                continue

            if unit.value == 'DO NOT COVER':
                continue

            if diag.ctype == 0 or unit.ctype == 0:
                continue

            if unit.value == 'U/C':
                continue

            diag, hc, frm, artime, unit, exam, comment = diag.value, hc.value, frm.value, artime.value, unit.value, exam.value, comment.value
            unit = int(unit)
            print(diag, unit)
            # arv = Arrival(station_id=id, diagram=diag, hc=hc, from_station=frm, arrival_time=artime, unit=unit, exam=exam)
            # s.add(arv)
        else:
            continue

    # Departures
    # print('DEPT')
    for nx in range(x+3, x+30):
        if sh.cell_type(nx, 8) not in (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK):
            row = sh.row(nx)[8:17]
            diag, hc, starttime, fd, time, miles, unit, comment, ontime = row

            if str(diag.value).strip() == '' and unit.value == '':
                break

            if str(diag.value).strip() == '' or unit.value == '':
                continue

            if diag.value == 'Diagram' or diag.value == 'Signed (Depot representative) :':
                break

            if diag.value == 'VSTP':
                continue

            if unit.ctype is xlrd.XL_CELL_TEXT:
                continue

            if unit.value == 'DO NOT COVER':
                continue

            if diag.ctype == 0 or unit.ctype == 0:
                continue

            if unit.value == 'U/C':
                continue

            diag, hc, starttime, fd, time, miles, unit, comment, ontime = diag.value, hc.value, starttime.value, fd.value, time.value, miles.value, unit.value, comment.value, ontime.value
            unit = int(unit)
            print(diag, unit)
            # dep = Departure(station_id=id, diagram=diag, hc=hc, finish_depot=fd, miles=miles, unit=unit, time=time)
            # s.add(dep)
        else:
            continue
    # s.commit()
