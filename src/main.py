from SpreadSheet import GetSpreadSheet
from SlackManager import PostMessage, PostCurrentPrice
from Crawler import getLowestPrice
import datetime as dt
from pytz import timezone

Date = dt.datetime.now(timezone('Asia/Seoul'))
Format_Date = Date.strftime('%Y/%m/%d %H시 %M분')

lowest_price = getLowestPrice()

worksheet = GetSpreadSheet()
worksheet_length = len(worksheet.get_values())
prev_lowest_price = worksheet.acell(
    "B" + str(worksheet_length)).value.removeprefix("₩").replace(",", "")

if (type(lowest_price) is int and lowest_price > 0):
    if (lowest_price < 600000):
        PostMessage(lowest_price)
    PostCurrentPrice(int(lowest_price), int(prev_lowest_price), Format_Date)
    worksheet.update_acell('A'+str(worksheet_length+1), str(Format_Date))
    worksheet.update_acell('B'+str(worksheet_length+1), f"₩{lowest_price:,}")
    print("스프레드 시트 업데이트 완료")
    print('A'+str(worksheet_length+1), str(Date))
    print('B'+str(worksheet_length+1), f"₩{lowest_price:,}")
else:
    print("Scrap Failed")
