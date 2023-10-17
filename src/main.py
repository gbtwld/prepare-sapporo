from SpreadSheet import getPrevPrices, UpdateSpreadSheet
from SlackManager import handleDiscountMessage, handlePriceChangeMessage
from Crawler import getLowestPrice
from Logging import getDate, log

prices = {
    "direct": 0,
    "layover": 0
}
prev_prices = getPrevPrices()
Date = getDate()

prices["direct"] = getLowestPrice("direct")
prices["layover"] = getLowestPrice("layover")

if (type(prices["direct"]) is int and prices["direct"] > 0 and type(prices["layover"]) is int and prices["layover"] > 0):
    if (prices["direct"] < 600000):
        handleDiscountMessage(prices["direct"])
    handlePriceChangeMessage(
        "direct", prices["direct"], prev_prices["direct"], Date)
    handlePriceChangeMessage(
        "layover", prices["layover"], prev_prices["layover"], Date)
    UpdateSpreadSheet(Date, prices)
else:
    log("Scrap Failed")
