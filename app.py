from audioop import add
from calendar import month
from distutils.spawn import spawn
from itertools import product
from posixpath import split
from models import (Base, session, Product, engine)
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


def clean_id(id_str, options):
    
    try:
        book_id = int(id_str)  
    
    except ValueError:
         input(""""
            \n ***** ID ERROR *****
            \r The ID numbers should be a number
            \r Press enter to try again.
            """
            )
    
    else:
        if book_id in options:
            return book_id
        
        else:
            input('''
            \n Pleae select from avaible options
            \r Press enter to try again.
            ''')
            return 

def add_product():
    pass 

def add_csv():
    with open('inventory.csv') as csvfile:
        data = csv.reader(csvfile)
        next(data)
        for row in data:
            product_in_db = (session.query(Product).filter(Product.product_name == row[0]).one_or_none())
            if product_in_db == None:
                product_name = row[0]
                product_price = clean_price(row[1])
                product_quantity = int(row[2])
                date_updated = clean_date(row[3])
                new_product = Product(product_name=product_name,
                                    product_price=product_price,
                                    product_quantity=product_quantity,
                                    date_updated=date_updated)
                session.add(new_product)
        
        session.commit()

def menu():

    choice = input('enter: v, a, b').lower()
    
    if choice == 'v':
        id_options = []
        for item in session.query(Product):
            id_options.append(item.product_id)
            

        
        print(id_options)





if __name__ == '__main__':
    # Base.metadata.create_all(engine)
    # add_csv()
    menu()

    

