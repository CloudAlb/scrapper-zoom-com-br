from bs4 import BeautifulSoup
import requests
import json
import locale

locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

# url_to_scrap = "https://www.zoom.com.br/celular/smartphone-samsung-galaxy-s24-ultra-5g-256gb-camera-quadrupla"
url_to_scrap = "https://www.zoom.com.br/celular/smartphone-samsung-galaxy-s24-ultra-5g-256gb-camera-quadrupla#historico-de-precos"
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

# getting cashback data

cashback_info_dict = price_history_text["props"]["initialReduxState"]["cashback"]

for key, value in cashback_info_dict.items():
    cashback_formula = value["cashback"]["formula"]
    merchant_id = cashback_formula["merchantId"]
    cashback_rate = cashback_formula["cashbackRate"]
    start_date = cashback_formula["startDate"]
    end_date = cashback_formula["endDate"]
    category = cashback_formula["category"]

    cashback_value = value["cashback"]["cashbackValue"]

# getting sellers data

sellers_data = {}

lowest_price_today_data = {}

product_name_data = ""

for idx, sellers_info_entry in enumerate(sellers_info_dict):
    product_name = sellers_info_entry["name"]  # might repeat itself through the dict

    image_url = sellers_info_entry["imageUrl"]  # might repeat itself through the dict

    price = sellers_info_entry["price"]

    seller_id = sellers_info_entry["sellerID"]
    seller_name = sellers_info_entry["sellerName"]
    seller_logo_url = sellers_info_entry["sellerLogoURL"]

    if seller_id not in sellers_data:
        sellers_data[seller_id] = {}

        sellers_data[seller_id]["name"] = seller_name
        sellers_data[seller_id]["logo_url"] = seller_logo_url

    if idx == 0:
        product_name_data = product_name
        lowest_price_today_data["price"] = price
        lowest_price_today_data["seller_id"] = seller_id

# getting price history data

price_history_data = next(iter(price_history_dict.values()))
price_history_arr = price_history_data["days"]

lowest_price_ever_data = {}

for idx, price_history_entry in enumerate(price_history_arr):
    product_id = price_history_entry["prodId"]  # repeats itself through the dict
    date = price_history_entry["date"]
    price = price_history_entry["price"]
    merchant_id = price_history_entry["merchantId"]

    if idx == 0:
        lowest_price_ever_data["price"] = price

    if price < lowest_price_ever_data["price"]:
        lowest_price_ever_data["date"] = date
        lowest_price_ever_data["price"] = price
        lowest_price_ever_data["merchant_id"] = merchant_id

lowest_price_today_seller_name = sellers_data[lowest_price_today_data["seller_id"]][
    "name"
]

lowest_price_ever_seller_name = "(unknown seller)"

try:
    lowest_price_ever_seller_name = sellers_data[lowest_price_ever_data["merchant_id"]][
        "name"
    ]
except Exception:
    pass

product_name_shortened = product_name.split(",")[0]
lowest_price_today_formatted = locale.currency(
    lowest_price_today_data["price"], grouping=True
)
lowest_price_ever_formatted = locale.currency(
    lowest_price_ever_data["price"], grouping=True
)

lowest_price_today_message = f'Today\'s lowest price for the "{product_name_shortened}" is: R$ {lowest_price_today_formatted}, from "{seller_name}"'
lowest_price_ever_message = f'The lowest **ever** recorded price was: R$ {lowest_price_ever_formatted}, on {lowest_price_ever_data['date']}, from "{lowest_price_ever_seller_name}"'

# print(lowest_price_today_message)
# print(lowest_price_ever_message)
