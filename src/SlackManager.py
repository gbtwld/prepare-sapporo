import os
from slack_sdk import WebClient
from dotenv import load_dotenv

load_dotenv(verbose=True)

SLACK_TOKEN = os.getenv('SLACK_TOKEN')

client = WebClient(token=SLACK_TOKEN)


def PostMessage(message):
    client.chat_postMessage(channel='#공습경보', text=message)
