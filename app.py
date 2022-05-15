from audioop import add
from calendar import month
from distutils.spawn import spawn
from posixpath import split
from models import (Base, Product, engine)
import datetime
import csv

def clean_price(price_str):
    
    
    
    try:
        split_price = float(price_str.split('$')[1])
    
    except ValueError:
        print("""
            \n  ***** Price ERROR *****
            \r The price input should include $
            \r Ex. $5.51
            \r Press enter to try again.
        """)
    
    else:
        print(int(split_price * 100))
    


def clean_date(date_str):
    
    split_date = date_str.split('/')
    
    try:

        month = int(split_date[0])
        day = int(split_date[1].split(',')[0])
        year = int(split_date[2])
        return_date = datetime.date(year,month, day)

    except ValueError:
        input(""""
            \n ***** DATE ERROR *****
            \r The date input should follow a valid format: Day/Month/Year
            \r Ex: 5/2/22
            \r Press enter to try again.
            """
            )
        return 
    
    else: 
        return return_date


def add_csv():
    with open('inventory.csv') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            # print(type(row[-1]))
            pass




if __name__ == '__main__':
    # Base.metadata.create_all(engine)
    # add_csv()
    # clean_date('9/22/2018')
    clean_price('$4.30')

