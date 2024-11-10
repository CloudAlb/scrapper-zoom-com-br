def call(price_history_dict, sellers_data, lowest_price_today_data):
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
        lowest_price_ever_seller_name = sellers_data[
            lowest_price_ever_data["merchant_id"]
        ]["name"]
    except Exception:
        pass

    return (
        price_history_data,
        lowest_price_ever_data,
        lowest_price_today_seller_name,
        lowest_price_ever_seller_name,
    )
