from selenium import webdriver
from selenium.webdriver.chrome.service import Service


url = ("https://dom.ria.com/uk/search/?category=1&realty_type=0&operation=1&state_id=12&price_cur=1&wo_dupl=1&sort="
       "inspected_sort&firstIteraction=false&limit=20&market=3&excludeSold=1&type=list&city_ids="
       "12&ch=242_239,247_252")

chrome_driver_path = '/home/denis/PycharmProjects/pythonProject/Diplom23/chromedriver/chromedriver'

service = Service(executable_path=chrome_driver_path)

chrome_options = webdriver.ChromeOptions()

browser = webdriver.Chrome(service=service, options=chrome_options)

try:
    browser.get(url=url)
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    browser.close()
    browser.quit()
