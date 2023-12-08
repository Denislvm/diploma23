from bs4 import BeautifulSoup
import requests
from time import sleep

from lxml import etree


def get_url():
    for count in range(1, 30):

        url = f"https://rem.ua/prodazha-kvartir-odessa?type=apartments&region=odesskaya&city=odessa&withoutSearchMarker=true&typeSort=rils&hasPhotos=1&currency=1&page={count}"

        response = requests.get(url)

        soup = BeautifulSoup(response.text, "lxml")

        data = soup.find_all('div', class_="object_block")

        for i in data:
            card_url = i.find("a", class_="object_block-link").get("href")
            yield card_url


def data():
    for card_url in get_url():

        webpage = requests.get(card_url)

        soup = BeautifulSoup(webpage.content, "html.parser")
        sleep(1)
        dom = etree.HTML(str(soup))

        price = dom.xpath('(//div[@class="d-flex flex-wrap justify-content-between"]/p[@class="object-price"]/span[@class="value"]/text())[1]')
        price_string = ''.join(price).replace("$", " ")

        street = dom.xpath('(//div[@class="col-md-4 data-char desktop-data-char object-info-desktop"]/p[@class="object-area"]/span[@class="value"]/text())[3]')
        street_string = "".join(street)

        district = dom.xpath('(//ul[@class="all-object-characteristic"]/li[@class="item"]/span[@class="value"]/text())[1]')
        district_string = ''.join(district)

        rooms = dom.xpath('(//ul[@class="all-object-characteristic"]/li[@class="item"]/span[@class="value"]/text())[2]')
        rooms_string = ''.join(rooms)

        total_area = dom.xpath('(//ul[@class="all-object-characteristic"]/li[@class="item"]/span[@class="value"]/text())[3]')
        total_area_string = ''.join(total_area)
        total_area_string_without_meters = total_area_string.replace("м²", " ")

        living_space = dom.xpath('(//ul[@class="all-object-characteristic"]/li[@class="item"]/span[@class="value"]/text())[4]')
        living_space_string = ''.join(living_space)

        area_kitchen = dom.xpath('(//ul[@class="all-object-characteristic"]/li[@class="item"]/span[@class="value"]/text())[5]')
        area_kitchen_string = ''.join(area_kitchen)

        floor = dom.xpath('(//ul[@class="all-object-characteristic"]/li[@class="item"]/span[@class="value"]/text())[6]')
        floor_string = ''.join(floor)

        total_floor_in_house = dom.xpath('(//ul[@class="all-object-characteristic"]/li[@class="item"]/span[@class="value"]/text())[7]')
        total_floor_in_house_string = ''.join(total_floor_in_house)

        house = dom.xpath('(//ul[@class="all-object-characteristic"]/li[@class="item"]/span[@class="value"]/text())[9]')
        house_string = ''.join(house)

        yield (district_string, street_string, rooms_string, total_area_string_without_meters, floor_string,
               total_floor_in_house_string, living_space_string, area_kitchen_string, house_string, price_string)




    # response = requests.get(card_url)
    #
    # soup = BeautifulSoup(response.text, "lxml")
    #
    # data = soup.find_all("div", class_="col-md-4 data-char desktop-data-char object-info-desktop")
    # for i in data:
    #
    #     price_with_dollar = i.find('p', class_="object-price").text
    #     price = price_with_dollar.replace("$", " ").replace("Цена:", " ")
    #
    #     district_w = i.find('p', class_='object-area').text
    #     district = district_w.replace("Район: ", " ")
    #
    #
    #     print(price, district)
# neighborhood = data.find("div", class_="all-characteristic")
    #
    # for i in neighborhood:
    #
    #     neighborhoo = i.find("span", class_='value').text
    #
    #     print(neighborhoo)



# with open("index.html", "w", encoding="utf-8") as f:
#      f.write(response.text)
