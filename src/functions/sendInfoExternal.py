def call(
    product_name_shortened,
    lowest_price_today_formatted,
    lowest_price_today_seller_name,
    lowest_price_ever_formatted,
    lowest_price_ever_date,
    lowest_price_ever_seller_name,
):
    lowest_price_today_message = f'Today\'s lowest price for the "{product_name_shortened}" is: R$ {lowest_price_today_formatted}, from "{lowest_price_today_seller_name}"'
    lowest_price_ever_message = f'The lowest **ever** recorded price was: R$ {lowest_price_ever_formatted}, on {lowest_price_ever_date}, from "{lowest_price_ever_seller_name}"'

    print(lowest_price_today_message)
    print(lowest_price_ever_message)
