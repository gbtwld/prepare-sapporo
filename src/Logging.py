import datetime as dt
from pytz import timezone


def getDate():
    Date = dt.datetime.now(timezone('Asia/Seoul')).strftime('%Y/%m/%d %H시 %M분')

    return Date


def log(message: str):
    Date = dt.datetime.now(timezone('Asia/Seoul')).strftime('%H:%M:%S')
    print(Date + " " + message)
