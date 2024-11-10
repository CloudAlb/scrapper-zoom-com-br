import locale


def call(
    sellers_info_dict,
    sellers_data,
    price_history_dict,
    lowest_price_today_data,
    lowest_price_ever_data,
):
    product_full_name = ""

    lowest_price_today_seller_name = sellers_data[lowest_price_today_data["seller_id"]][
        "name"
    ]

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

    lowest_price_today_message = f'Today\'s lowest price for the "{product_name_shortened}" is: R$ {lowest_price_today_formatted}, from "{lowest_price_today_seller_name}"'
    lowest_price_ever_message = f'The lowest **ever** recorded price was: R$ {lowest_price_ever_formatted}, on {lowest_price_ever_data['date']}, from "{lowest_price_ever_seller_name}"'

    print(lowest_price_today_message)
    print(lowest_price_ever_message)

    return lowest_price_today_seller_name, lowest_price_ever_seller_name
