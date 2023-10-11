import os
from slack_sdk import WebClient
from dotenv import load_dotenv

load_dotenv(verbose=True)

SLACK_TOKEN = os.getenv('SLACK_TOKEN')

client = WebClient(token=SLACK_TOKEN)


def PostMessage(price: int):
    message = "🚨공습경보🚨 항공권 가격이 " + str(price) + "원 입니다!!! 얼른 구입하세요!!!!"
    client.chat_postMessage(channel='#공습경보', text=message)


def PostCurrentPrice(curPrice: int, prevPrice: int, date: str):
    curPriceFormat = f"{curPrice:,}"
    rate = round((curPrice - prevPrice) / prevPrice * 100, 2)
    rate_string = str(rate) if rate < 0 else "+" + str(rate)
    message = date + " 현재 항공권 가격은 " + \
        curPriceFormat + "원 입니다. (" + rate_string + "%)"
    if (rate != 0):
        client.chat_postMessage(channel='#가격변동', text=message)
    else:
        print("가격 변동 없음")
