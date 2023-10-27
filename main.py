import requests
from bs4 import BeautifulSoup
from useful_information import cookies, headers


main_url = 'https://dom.ria.com/uk/search/?excludeSold=1&category=1&realty_type=0&operation=1&state_id=12&price_cur=1&wo_dupl=1&sort=inspected_sort&firstIteraction=false&city_ids=12&client=searchV2&limit=20&type=list&ch=242_239,247_252'


def get_soup(url):
    response = requests.get(
        url,
        cookies=cookies,
        headers=headers,
    )
    return BeautifulSoup(response.text, 'html.parser')


def main_parser():
    product_data = get_soup(main_url)

    all_product = product_data.findAll('div', class_='search-result-list f100-wrap')
