from SpreadSheet import GetSpreadSheet
from SlackManager import PostMessage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime as dt
from pytz import timezone

URL = "https://flight.naver.com/flights/international/ICN-SPK-20240118/SPK-ICN-20240122?adult=5&isDirect=true&fareType=Y"

lowest_price = 0
Date = dt.datetime.now(timezone('Asia/Seoul'))
Format_Date = Date.strftime('%Y/%m/%d %H시 %M분')

options = webdriver.ChromeOptions()
options.add_argument("--headless=chrome")
options.add_argument('incognito')

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(3)

try:
    worksheet = GetSpreadSheet()
    worksheet_length = len(worksheet.get_values())

    driver.get(URL)

    wait = WebDriverWait(driver, 30)

    WebDriverWait(driver, 5
                  ).until(EC.presence_of_element_located((By.CLASS_NAME, "loadingProgress_loadingProgress__1LRJo")))

    # then wait for the element to disappear
    WebDriverWait(driver, 30
                  ).until_not(EC.presence_of_element_located((By.CLASS_NAME, "loadingProgress_loadingProgress__1LRJo")))

    elements = driver.find_elements(By.CLASS_NAME, "item_num__3R0Vz")

    for elem in elements:
        elem_to_int = int(elem.get_attribute(
            'innerText').replace(",", ""))
        if (lowest_price == 0 or lowest_price > elem_to_int):
            lowest_price = elem_to_int

    lowest_price = 200000
    if (lowest_price < 600000):
        PostMessage("🚨테스트🚨 항공권 가격이 " + str(lowest_price) + " 입니다!!! 얼른 구입하세요!!!!")

    lowest_price = f"₩{lowest_price:,}"

    if (lowest_price != "₩0"):
        worksheet.update_acell('A'+str(worksheet_length+1), str(Format_Date))
        worksheet.update_acell('B'+str(worksheet_length+1), lowest_price)
        print("스프레드 시트 업데이트 완료")
        print('A'+str(worksheet_length+1), str(Date))
        print('B'+str(worksheet_length+1), lowest_price)
    else:
        print("Scrap Fail")

except Exception as e:
    print(e)

finally:
    print("end")
