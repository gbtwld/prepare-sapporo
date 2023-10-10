from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://flight.naver.com/flights/international/ICN-SPK-20240118/SPK-ICN-20240122?adult=5&isDirect=true&fareType=Y"


def getLowestPrice():
    lowest_price = 0

    options = webdriver.ChromeOptions()
    options.add_argument("--headless=chrome")
    options.add_argument('incognito')

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(URL)

        driver.implicitly_wait(3)
        WebDriverWait(driver, 30
                      ).until_not(EC.presence_of_element_located((By.CLASS_NAME, "loadingProgress_loadingProgress__1LRJo")))

        elements = driver.find_elements(By.CLASS_NAME, "item_num__3R0Vz")
        for elem in elements:
            elem_to_int = int(elem.get_attribute(
                'innerText').replace(",", ""))
            if (lowest_price == 0 or lowest_price > elem_to_int):
                lowest_price = elem_to_int
        return lowest_price

    except Exception as e:
        print(e)

    finally:
        print("Crawling Result: " + str(lowest_price))
