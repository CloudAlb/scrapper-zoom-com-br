from bs4 import BeautifulSoup
import requests
import json
import locale

from functions import (
    retrieveCashbackData,
    retrieveSellersData,
    retrievePriceHistoryData,
    getProductInterestInfo,
    sendInfoExternal,
)

locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

url_to_scrap = "https://www.zoom.com.br/celular/smartphone-samsung-galaxy-s24-ultra-5g-256gb-camera-quadrupla"
url_html_raw = requests.get(url_to_scrap).text

soup = BeautifulSoup(url_html_raw, "lxml")

html_raw_parent_tag = soup.find("script", {"id": "__NEXT_DATA__"})

if not html_raw_parent_tag:
    raise Exception("Data not found")

price_history_text = json.loads(html_raw_parent_tag.text)

price_history_dict = price_history_text["props"]["initialReduxState"]["priceHistory"][
    "priceHistory"
]

sellers_info_dict = price_history_text["props"]["initialReduxState"]["offers"][
    "displayOffers"
]

cashback_data = retrieveCashbackData.call(price_history_text)

sellers_data, product_full_name, lowest_price_today_data = retrieveSellersData.call(
    sellers_info_dict
)

(
    price_history_data,
    lowest_price_ever_data,
    lowest_price_today_seller_name,
) = retrievePriceHistoryData.call(
    price_history_dict, sellers_data, lowest_price_today_data
)

(
    product_name_shortened,
    lowest_price_today_formatted,
    lowest_price_ever_seller_name,
    lowest_price_ever_formatted,
    lowest_price_ever_date_formatted,
) = getProductInterestInfo.call(
    product_full_name,
    sellers_info_dict,
    sellers_data,
    lowest_price_ever_data,
    lowest_price_today_data,
    lowest_price_ever_data,
)

sendInfoExternal.call(
    product_name_shortened,
    lowest_price_today_formatted,
    lowest_price_today_seller_name,
    lowest_price_ever_formatted,
    lowest_price_ever_date_formatted,
    lowest_price_ever_seller_name,
)
