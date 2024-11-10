def call(price_history_text):
    cashback_info_dict = price_history_text["props"]["initialReduxState"]["cashback"]

    for key, value in cashback_info_dict.items():
        cashback_formula = value["cashback"]["formula"]
        merchant_id = cashback_formula["merchantId"]
        cashback_rate = cashback_formula["cashbackRate"]
        start_date = cashback_formula["startDate"]
        end_date = cashback_formula["endDate"]
        category = cashback_formula["category"]

        cashback_value = value["cashback"]["cashbackValue"]
