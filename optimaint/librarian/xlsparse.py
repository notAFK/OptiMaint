import xlrd


ABRV = ['EC', 'XW', 'MA', 'CZ', 'BK', 'LA', 'PZ', 'EH']


def parse_sheet(sh):
    # print('  ', sh.name, sh.nrows, sh.ncols)
    for rx in range(sh.nrows):
        rval = sh.cell_value(rowx=rx, colx=8)
        if rval in ABRV:
            parse_location(sh, rx, 0)


def parse_location(sh, x, y):
    id = sh.cell_value(rowx=x, colx=8)
    name = sh.cell_value(rowx=x, colx=0).split('(')[0]

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

            if diag.value == 'Diagram':
                break

            if diag.ctype == 0 or unit.ctype == 0:
                continue

            if unit.value == 'U/C':
                continue

            print(diag, unit)
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

            if diag.ctype == 0 or unit.ctype == 0:
                continue

            if unit.value == 'U/C':
                continue

            print(diag, unit)
        else:
            break


def parse_row():
    pass
