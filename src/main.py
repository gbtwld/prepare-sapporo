from SpreadSheet import GetSpreadSheet, UpdateSpreadSheet
from SlackManager import PostMessage, PostCurrentPrice
from Crawler import getLowestPrice
import datetime as dt
from pytz import timezone

Date = dt.datetime.now(timezone('Asia/Seoul'))
Format_Date = Date.strftime('%Y/%m/%d %H시 %M분')

lowest_price = getLowestPrice()

worksheet = GetSpreadSheet()
worksheet_length = len(worksheet.get_values())
prev_lowest_price = int(worksheet.acell(
    "B" + str(worksheet_length)).value.removeprefix("₩").replace(",", ""))

if (type(lowest_price) is int and lowest_price > 0):
    if (lowest_price < 600000):
        PostMessage(lowest_price)
    PostCurrentPrice(lowest_price, prev_lowest_price, Format_Date)
    UpdateSpreadSheet(worksheet_length, Format_Date, lowest_price)
else:
    print("Scrap Failed")
