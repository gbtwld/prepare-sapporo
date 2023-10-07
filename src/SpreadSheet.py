from oauth2client.service_account import ServiceAccountCredentials
import gspread


def GetSpreadSheet():
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    json = 'prepare-sapporo-fcfcb0410910.json'
    credentials = ServiceAccountCredentials.from_json_keyfile_name(json, scope)
    gc = gspread.authorize(credentials)
    sheet_url = 'https://docs.google.com/spreadsheets/d/14ZqCqKH22KhdvNPEa5efYpn-fmsUkIv-TuHX2TIfoHU/edit#gid=0'
    doc = gc.open_by_url(sheet_url)
    worksheet = doc.worksheet('일별가격')

    return worksheet
