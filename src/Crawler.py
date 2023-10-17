from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Logging import log

DIRECT_URL = "https://flight.naver.com/flights/international/ICN-SPK-20240118/SPK-ICN-20240122?adult=5&isDirect=true&fareType=Y"

LAYOVER_URL = "https://flight.naver.com/flights/international/SEL-SPK-20240118/SPK-TYO-20240121/TYO-SEL-20240122?adult=5&fareType=Y"

options = webdriver.ChromeOptions()
options.add_argument("--headless=chrome")
options.add_argument('incognito')

driver = webdriver.Chrome(options=options)


def getLowestPrice(fareType: str):
    lowest_price = 0
    try:
        driver.get(DIRECT_URL if fareType == "direct" else LAYOVER_URL)
        log("[크롤링 시작] " + "직항" if fareType == "direct" else "[크롤링 시작] " + "경유")
        driver.implicitly_wait(3)

        WebDriverWait(driver, 60
                      ).until_not(EC.presence_of_element_located((By.CLASS_NAME, "progressBar_progress__2VAEK")))

        price_element = driver.find_element(By.CLASS_NAME, "item_num__3R0Vz")

        lowest_price = int(price_element.get_attribute(
            'innerText').replace(",", ""))
        log("[크롤링 종료] " + "직항" if fareType == "direct" else "[크롤링 종료] " + "경유")

        return lowest_price

    except Exception as e:
        print(e)

    finally:
        log("[크롤링 결과] " + "직항 " + str(lowest_price) if fareType ==
            "direct" else "[크롤링 결과] " + "경유 " + str(lowest_price))
