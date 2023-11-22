from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

import time

list_of_apartments = []

# parsing completed on 25 page.
# https://dom.ria.com/uk/search/?category=1&realty_type=0&operation=1&state_id=12&price_cur=1&wo_dupl=1&sort=inspected_sort&firstIteraction=false&limit=20&market=3&excludeSold=1&type=list&city_ids=12&ch=242_239,247_252
url = "https://dom.ria.com/uk/search/?excludeSold=1&category=1&realty_type=0&operation=1&state_id=12&price_cur=1&wo_dupl=1&sort=inspected_sort&firstIteraction=false&limit=20&market=3&type=list&city_ids=12&client=searchV2&page=24&ch=242_239,247_252"

# binary, service, options
binary = FirefoxBinary('/firefoxdriver/geckodriver')

service = Service(firefox_binary=binary)
options = webdriver.FirefoxOptions()

# driver
driver = webdriver.Firefox(service=service, options=options)

try:
    driver.get(url=url)
    time.sleep(5)

    price_elements = driver.find_elements(By.XPATH, "//b[@class='size22']")
    price_for_meters = driver.find_elements(By.XPATH, "//span[@class='size14 point-before']")
    rooms_count = driver.find_elements(By.XPATH, "//span[@class='point-before'][1]")
    meters_in_apartments = driver.find_elements(By.XPATH, "//span[@class='point-before'][2]")
    floors = driver.find_elements(By.XPATH, "//span[@class='point-before'][3]")
    neighborhoods = driver.find_elements(By.XPATH, "//span[@class='mb-5 i-block v-middle'][1]")
    streets = driver.find_elements(By.XPATH, "//a[@class='realty-link size22 bold break']")

    for i in range(len(price_elements)):
        apartment_data = {
            "price": price_elements[i].text,
            "price_for_meter": price_for_meters[i].text,
            "rooms": rooms_count[i].text,
            "meters_in_apartments": meters_in_apartments[i].text,
            "floors": floors[i].text,
            "neighborhood": neighborhoods[i].text,
            "street": streets[i].text
        }
        list_of_apartments.append(apartment_data)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()


with open('apartments_data.json', 'a', encoding='utf-8') as file:
    for apartment in list_of_apartments:
        file.write(str(apartment) + '\n')

print(list_of_apartments)