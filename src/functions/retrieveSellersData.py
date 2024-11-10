def call(sellers_info_dict):
    lowest_price_today_data = {}
    sellers_data = {}
    product_full_name = ""

    for idx, sellers_info_entry in enumerate(sellers_info_dict):
        seller_id = sellers_info_entry["sellerID"]
        seller_name = sellers_info_entry["sellerName"]
        seller_logo_url = sellers_info_entry["sellerLogoURL"]

        if seller_id not in sellers_data:
            sellers_data[seller_id] = {}

            sellers_data[seller_id]["name"] = seller_name
            sellers_data[seller_id]["logo_url"] = seller_logo_url

        seller_id = sellers_info_entry["sellerID"]
        product_name = sellers_info_entry[
            "name"
        ]  # might repeat itself through the dict
        image_url = sellers_info_entry[
            "imageUrl"
        ]  # might repeat itself through the dict
        price = sellers_info_entry["price"]

        if idx == 0:
            product_full_name = product_name
            lowest_price_today_data["price"] = price
            lowest_price_today_data["seller_id"] = seller_id

    return sellers_data, product_full_name, lowest_price_today_data
