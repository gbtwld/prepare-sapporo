from SpreadSheet import GetSpreadSheet, UpdateSpreadSheet
from SlackManager import PostMessage, PostCurrentPrice
from Crawler import getLowestPrice
from Logging import getDate, log

Date = getDate()
lowest_price = getLowestPrice()

worksheet = GetSpreadSheet()
worksheet_length = len(worksheet.get_values())
prev_lowest_price = int(worksheet.acell(
    "B" + str(worksheet_length)).value.removeprefix("₩").replace(",", ""))

if (type(lowest_price) is int and lowest_price > 0):
    if (lowest_price < 600000):
        PostMessage(lowest_price)
    # PostCurrentPrice(lowest_price, prev_lowest_price, Date)
    UpdateSpreadSheet(worksheet_length, Date, lowest_price)
else:
    log("Scrap Failed")
