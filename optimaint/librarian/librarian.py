import os
import sys
import xlrd

import optimaint.librarian.xlsparse as xlsparse


DATA_DIR = os.path.abspath('history/2017')
MONTH_LIST = ['july', 'august', 'september', 'october', 'november']


def parse_week(week):
    week_book = xlrd.open_workbook(week)

    if week_book.nsheets != 12:
        print('Why is the number of sheets not 12?!')
        sys.exit()

    print(week[-15:])

    for sindex in range(1, 8):
        xlsparse.parse_sheet(week_book.sheet_by_index(sindex))


def parse_month(month):
    fp = os.path.join(DATA_DIR, month)
    for week in os.listdir(fp):
        pn_week = week.lower().strip()
        if pn_week.startswith('week') and pn_week.endswith('.xls') and len(pn_week) < 17:
            parse_week(os.path.join(fp, week))


def parse_all():
    for month in MONTH_LIST:
        parse_month(month)


parse_all()
