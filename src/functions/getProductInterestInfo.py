import locale
from datetime import datetime


def call(
    product_full_name,
    sellers_info_dict,
    sellers_data,
    price_history_dict,
    lowest_price_today_data,
    lowest_price_ever_data,
):
    lowest_price_ever_seller_name = "(unknown seller)"
    try:
        lowest_price_ever_seller_name = sellers_data[
            lowest_price_ever_data["merchant_id"]
        ]["name"]
    except Exception:
        pass

    product_name_shortened = product_full_name.split(",")[0]

    lowest_price_today_formatted = locale.currency(
        lowest_price_today_data["price"], grouping=True
    )
    lowest_price_ever_formatted = locale.currency(
        lowest_price_ever_data["price"], grouping=True
    )

    lowest_price_ever_date = lowest_price_ever_data["date"]
    lowest_price_ever_date_obj = datetime.strptime(lowest_price_ever_date, "%Y-%m-%d")
    lowest_price_ever_date_formatted = lowest_price_ever_date_obj.strftime("%d/%m/%Y")

    return (
        product_name_shortened,
        lowest_price_today_formatted,
        lowest_price_ever_seller_name,
        lowest_price_ever_formatted,
        lowest_price_ever_date_formatted,
    )
