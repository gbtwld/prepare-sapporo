import os
from slack_sdk import WebClient
from dotenv import load_dotenv
from Logging import log

load_dotenv(verbose=True)

SLACK_TOKEN = os.getenv('SLACK_TOKEN')

client = WebClient(token=SLACK_TOKEN)


def handleDiscountMessage(price: int):
    message = "🚨공습경보🚨 항공권 가격이 " + str(price) + "원 입니다!!! 얼른 구입하세요!!!!"
    client.chat_postMessage(channel='#공습경보', text=message)
    log("[공습경보 발송]")


def handlePriceChangeMessage(fareType: str, curPrice: int, prevPrice: int, date: str):
    curPriceFormat = f"{curPrice:,}"
    rate = round((curPrice - prevPrice) / prevPrice * 100, 2)
    rate_string = str(rate) if rate < 0 else "+" + str(rate)
    message = "[직항] " if fareType == "direct" else "[경유] "
    message += "현재 항공권 가격은 " + curPriceFormat + "원 입니다. (" + rate_string + "%)"
    if (rate != 0):
        client.chat_postMessage(channel='#가격변동', text=message)
        log("[가격변동 메시지 발송]" + message)
    else:
        log("가격 변동 없음")
