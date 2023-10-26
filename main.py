import requests
from bs4 import BeautifulSoup


cookies = {
    'ui': '9bc515b06398476a',
    '_ga': 'GA1.3.537098800.1679006885',
    '__uzma': '0fa3bf4d-1e33-44f1-9813-d77ee489c55b',
    '__uzmb': '1698239198',
    '__uzme': '9599',
    '_gcl_au': '1.1.1071719198.1698239199',
    '_gid': 'GA1.3.991355387.1698239199',
    '_ga': 'GA1.1.537098800.1679006885',
    '_fbp': 'fb.1.1698239199673.1532180612',
    'dom_sess': '1x3-apct6VyFwFx07KUtd5hDRwCBc_3C',
    'pageCount': '4',
    '_ga_HJZP5P77GH': 'GS1.1.1698239199.2.1.1698239266.59.0.0',
    '_gat_UA-87766776-1': '1',
    '_gat_UA-87766776-22': '1',
    '__uzmd': '1698239266',
    '__uzmc': '295072879817',
}

headers = {
    'authority': 'dom.ria.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'ui=9bc515b06398476a; _ga=GA1.3.537098800.1679006885; __uzma=0fa3bf4d-1e33-44f1-9813-d77ee489c55b; __uzmb=1698239198; __uzme=9599; _gcl_au=1.1.1071719198.1698239199; _gid=GA1.3.991355387.1698239199; _ga=GA1.1.537098800.1679006885; _fbp=fb.1.1698239199673.1532180612; dom_sess=1x3-apct6VyFwFx07KUtd5hDRwCBc_3C; pageCount=4; _ga_HJZP5P77GH=GS1.1.1698239199.2.1.1698239266.59.0.0; _gat_UA-87766776-1=1; _gat_UA-87766776-22=1; __uzmd=1698239266; __uzmc=295072879817',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
}


def get_soup(url):
    response = requests.get(
        'https://dom.ria.com/uk/search/?excludeSold=1&category=1&realty_type=0&operation=1&state_id=12&price_cur=1&wo_dupl=1&sort=inspected_sort&firstIteraction=false&city_ids=12&client=searchV2&limit=20&type=list&ch=242_239,247_252',
        cookies=cookies,
        headers=headers,
    )