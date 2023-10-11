from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://flight.naver.com/flights/international/ICN-SPK-20240118/SPK-ICN-20240122?adult=5&isDirect=true&fareType=Y"

options = webdriver.ChromeOptions()
options.add_argument("--headless=chrome")
options.add_argument('incognito')

driver = webdriver.Chrome(options=options)


def getLowestPrice():
    lowest_price = 0
    try:
        driver.get(URL)
        driver.implicitly_wait(3)

        WebDriverWait(driver, 30
                      ).until_not(EC.presence_of_element_located((By.CLASS_NAME, "progressBar_progress__2VAEK")))

        price_element = driver.find_element(By.CLASS_NAME, "item_num__3R0Vz")

        lowest_price = int(price_element.get_attribute(
            'innerText').replace(",", ""))

        return lowest_price

    except Exception as e:
        print(e)

    finally:
        print("[크롤링 결과] " + str(lowest_price))
