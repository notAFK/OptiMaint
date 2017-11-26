import os
import sys
import xlrd

import optimaint.librarian.xlsparse as xlsparse


DATA_DIR_2017 = os.path.abspath('history/2017')
DATA_DIR_2016 = os.path.abspath('history/2016')
DATA_DIR_2015 = os.path.abspath('history/2015')
MONTH_LIST = ['july', 'august', 'september', 'october']


def parse_week(week):
    week_book = xlrd.open_workbook(week)
    if week.endswith('.DS_Store'):
        return

    if week_book.nsheets != 12:
        return

    print('---------', week[-14:-4], '---------')

    for sindex in range(1, 8):
        xlsparse.parse_sheet(week_book, week_book.sheet_by_index(sindex))


def parse_month(data_set):
    print(data_set)
    if data_set.endswith('.DS_Store'):
        return
    for week in os.listdir(data_set):
        pn_week = week.lower().strip()
        if pn_week.startswith('week') and pn_week.endswith('.xls') and len(pn_week) < 17:
            parse_week(os.path.join(data_set, week))


def parse_all():
    for dir in os.listdir(DATA_DIR_2015):
        print(dir)
        parse_month(os.path.join(DATA_DIR_2015, dir))
    for dir in os.listdir(DATA_DIR_2016):
        parse_month(os.path.join(DATA_DIR_2016, dir))
    for month in MONTH_LIST:
        parse_month(os.path.join(DATA_DIR_2017, month))


parse_all()
