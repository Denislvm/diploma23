from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

import time

list_of_apartments = []

# https://realting.com/ru/property-for-sale/ukraine/odesa?movemap-input=1&slug=property-for-sale&search=%D0%9E%D0%B4%D0%B5%D1%81%D1%81%D0%B0&Estate%5Bgeo_id%5D=178214&Estate%5Bcurrency%5D=EUR&Estate%5Bzoom%5D=11&Estate%5Bx1%5D=30.50011&Estate%5By1%5D=46.27578&Estate%5Bx2%5D=30.97939&Estate%5By2%5D=46.69796&referrer_id=&sort=-created_at
url = "https://realting.com/ru/property-for-sale/ukraine/odesa?movemap-input=1&slug=property-for-sale&search=%D0%9E%D0%B4%D0%B5%D1%81%D1%81%D0%B0&Estate%5Bgeo_id%5D=178214&Estate%5Bcurrency%5D=EUR&Estate%5Bzoom%5D=11&Estate%5Bx1%5D=30.50011&Estate%5By1%5D=46.27578&Estate%5Bx2%5D=30.97939&Estate%5By2%5D=46.69796&referrer_id=&sort=-created_at"

# binary, service, options
binary = FirefoxBinary('/home/denis/PycharmProjects/pythonProject/Diplom23/firefoxdriver/geckodriver')

service = Service(firefox_binary=binary)
options = webdriver.FirefoxOptions()

# driver
driver = webdriver.Firefox(service=service, options=options)

try:
    driver.get(url=url)
    time.sleep(10)

    price_elements = driver.find_elements(By.XPATH, "//div[@class='price-item']")
    rooms_count = driver.find_elements(By.XPATH, "//div[@title='Комнаты']")
    count_bathroom = driver.find_elements(By.XPATH, "//div[@title='Кол-во ванных комнат']")
    meters_in_apartments = driver.find_elements(By.XPATH, "//div[@title='Площадь']")
    floors = driver.find_elements(By.XPATH, "//div[@title='Количество этажей']")
    # neighborhoods = driver.find_elements(By.XPATH, "//span[@class='mb-5 i-block v-middle'][1]")
    # streets = driver.find_elements(By.XPATH, "//a[@class='realty-link size22 bold break']")
    min_length = min(len(price_elements), len(rooms_count), len(count_bathroom), len(meters_in_apartments), len(floors))

    for i in range(min_length):
        apartment_data = {
            "price": price_elements[i].text,
            "rooms": rooms_count[i].text,
            "count_bathroom": count_bathroom[i].text,
            "meters_in_apartments": meters_in_apartments[i].text,
            "floors": floors[i].text,
            # "neighborhood": neighborhoods[i].text,
            # "street": streets[i].text
        }
        list_of_apartments.append(apartment_data)
        # print(list_of_apartments)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

#
with open('apartments_data.json', 'w', encoding='utf-8') as file:
    for apartment in list_of_apartments:
        file.write(str(apartment) + '\n')
