from oauth2client.service_account import ServiceAccountCredentials
import gspread
from Logging import log

SCOPE = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
JSON = 'prepare-sapporo-fcfcb0410910.json'
CREDENTIALS = ServiceAccountCredentials.from_json_keyfile_name(JSON, SCOPE)
SHEET_URL = 'https://docs.google.com/spreadsheets/d/14ZqCqKH22KhdvNPEa5efYpn-fmsUkIv-TuHX2TIfoHU/edit#gid=0'

gc = gspread.authorize(CREDENTIALS)
doc = gc.open_by_url(SHEET_URL)

direct_worksheet = doc.worksheet('직항')
layover_worksheet = doc.worksheet('경유')

direct_worksheet_length = len(direct_worksheet.get_values())
layover_worksheet_length = len(layover_worksheet.get_values())


def getPrevPrices():
    prev_prices = {
        "direct": int(direct_worksheet.acell(
            "B" + str(direct_worksheet_length)).value.removeprefix("₩").replace(",", "")),
        "layover": int(layover_worksheet.acell(
            "B" + str(layover_worksheet_length)).value.removeprefix("₩").replace(",", ""))
    }
    return prev_prices


def UpdateSpreadSheet(date: str, prices):
    direct_worksheet.update_acell('A'+str(direct_worksheet_length+1), date)
    direct_worksheet.update_acell(
        'B'+str(direct_worksheet_length+1), f"₩{prices['direct']:,}")
    layover_worksheet.update_acell('A'+str(layover_worksheet_length+1), date)
    layover_worksheet.update_acell(
        'B'+str(layover_worksheet_length+1), f"₩{prices['layover']:,}")
    log("[스프레드 시트 업데이트 완료]")
