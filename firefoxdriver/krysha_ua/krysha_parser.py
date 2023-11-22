# https://odessa.krysha.ua/kupit-odessa.html

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

import time

list_of_apartments = []

url = "https://odessa.krysha.ua/kupit-odessa.html"

binary = FirefoxBinary('/home/denis/PycharmProjects/pythonProject/Diplom23/firefoxdriver/geckodriver')

service = Service(firefox_binary=binary)
options = webdriver.FirefoxOptions()



driver = webdriver.Firefox(service=service, options=options)

try:
    driver.get(url=url)
    time.sleep(1)

    name = driver.find_elements(By.XPATH, "//span[@itemprop='name']")
    price_elements = driver.find_elements(By.XPATH, "//span[@class='price__total']")
    rooms_count = driver.find_elements(By.XPATH, "//div[@title='Комнаты']")
    count_bathroom = driver.find_elements(By.XPATH, "//div[@title='Кол-во ванных комнат']")
    meters_in_apartments = driver.find_elements(By.XPATH, "//div[@title='Площадь']")
    floors = driver.find_elements(By.XPATH, "//div[@title='Количество этажей']")
    # neighborhoods = driver.find_elements(By.XPATH, "//span[@class='mb-5 i-block v-middle'][1]")
    # streets = driver.find_elements(By.XPATH, "//a[@class='realty-link size22 bold break']")

    for i in range(len(name)):
        apartment_data = {
            "name": name[i].text,
            "price": price_elements[i].text,
            # "rooms": rooms_count[i].text,
            # "count_bathroom": count_bathroom[i].text,
            # "meters_in_apartments": meters_in_apartments[i].text,
            # "floors": floors[i].text,
            # "neighborhood": neighborhoods[i].text,
            # "street": streets[i].text
        }
        list_of_apartments.append(apartment_data)
        print(apartment_data)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

#
with open('apartments_data.json', 'w', encoding='utf-8') as file:
    for apartment in list_of_apartments:
        file.write(str(apartment) + '\n')
