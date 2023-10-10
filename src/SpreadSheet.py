from oauth2client.service_account import ServiceAccountCredentials
import gspread

SCOPE = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
JSON = 'prepare-sapporo-fcfcb0410910.json'
CREDENTIALS = ServiceAccountCredentials.from_json_keyfile_name(JSON, SCOPE)
SHEET_URL = 'https://docs.google.com/spreadsheets/d/14ZqCqKH22KhdvNPEa5efYpn-fmsUkIv-TuHX2TIfoHU/edit#gid=0'

gc = gspread.authorize(CREDENTIALS)
doc = gc.open_by_url(SHEET_URL)
worksheet = doc.worksheet('일별가격')


def GetSpreadSheet():
    return worksheet


def UpdateSpreadSheet(sheet_length: int, date: str, price: int):
    worksheet.update_acell('A'+str(sheet_length+1), date)
    worksheet.update_acell('B'+str(sheet_length+1), f"₩{price:,}")
    print("스프레드 시트 업데이트 완료")
    print('A'+str(sheet_length+1), date)
    print('B'+str(sheet_length+1), f"₩{price:,}")
