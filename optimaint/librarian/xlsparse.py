
ABRV = ['EC', 'XW', 'MA', 'CZ', 'BK', 'LA', 'PZ', 'EH']


def parse_sheet(sh):
    print('  ', sh.name, sh.nrows, sh.ncols)
    for rx in range(sh.nrows):
        rval = sh.cell_value(rowx=rx, colx=8)
        if rval in ABRV:
            print(rval)


def parse_location():
    pass


def parse_row():
    pass
