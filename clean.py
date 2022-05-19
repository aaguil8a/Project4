import datetime


def clean_date(date_str):
    split_date = date_str.split('/')
    try:
        month = int(split_date[0])
        day = int(split_date[1])
        year = int(split_date[2])
        return_date = datetime.date(year, month, day)
    except ValueError:
        input('''
            \n ***** DATE ERROR *****
            \rThe date from should include a format: Ex. 5/19/2021
            \rPress [ENTER] to try again.''')
        return
    else:
        return return_date


def clean_price(price_str):
    try:
        price_float = float(price_str.split('$')[1])
    except IndexError:
        input('''
            \n***** PRICE ERROR *****
            \rThe price should have $ sign: Ex., $9.52
            \rPress [ENTER] to try again.''')
    except ValueError:
        input('''
            \n***** PRICE ERROR *****
            \rThe price should have $ sign: Ex., $2.52
            \rPress [ENTER] to try again.''')
    else:
        return int(price_float * 100)


def clean_id(id_str, options):
    try:
        selected_product_id = int(id_str)
    except ValueError:
        input('''
            \n***** ID ERROR *****
            \rThe id should be a whole number: Ex., 5
            \rPress [ENTER] to try again.''')
        return
    else:
        if selected_product_id in options:
            return selected_product_id
        else:
            input(f'''
                \n***** ID ERROR *****
                \r'Please select a product number within range {options[0]} - {options[-1]}'
                \rPress [ENTER] to try again.''')
            return
