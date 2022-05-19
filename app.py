from audioop import add
from calendar import month
from distutils.spawn import spawn
from itertools import product
from posixpath import split
from secrets import choice
from models import (Base, session, Product, engine)
import datetime
import csv

########################### 
def clean_price(price_str):

    try:
        if price_str[0] != '$':
            raise ValueError

        split_price = float(price_str.split('$')[1])
        split_int = int(split_price * 100)
    
    except ValueError:
        input("""
            \n  ***** Price ERROR *****
            \r The price input should include $
            \r Ex. $5.51
            \r Press enter to try again.
        """)

    else:
        return split_int
    


def clean_date(date_str):
    try:
        split_date = date_str.split('/')
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

def clean_quantity(quantity_str):
    try:
        quantity_int = int(quantity_str)
    except ValueError:
           input(""""
            \n ***** Quantity ERROR *****
            \r The input as to be an integer
            \r Ex: 11
            \r Press enter to try again.
            """
            )
    else:
        return quantity_int

##########################################################

def add_csv():
    with open('inventory.csv') as csvfile:
        data = csv.reader(csvfile)
        next(data)
        for row in data:
            product_in_db = (session.query(Product).filter(Product.product_name == row[0]).one_or_none())
            if product_in_db == None:
                product_name = row[0]
                product_price = clean_price(row[1])
                product_quantity = clean_quantity(row[2])
                date_updated = clean_date(row[3])
                new_product = Product(product_name=product_name,
                                    product_price=product_price,
                                    product_quantity=product_quantity,
                                    date_updated=date_updated)
                session.add(new_product)
        
        session.commit()


def menu():
    while True:
        print('''
            \nProducts 
            \rv) view all products
            \ra) add new product
            \rb) create backup
            \re) Exit
        
        
        ''')
        choice =  input('What would you like to do?')
        if choice in ['v','a','b','e']:
            return choice
        else:
            print('Please choose one of the options above. Press to enter again')


def app():
    app_running = True
    while app_running:
        choice = menu()
        if choice == 'v':
            # view all products
            pass
        
        elif choice == 'a':
            # add new product
            
            # product name 
            product_name = input('Name: ')
            
            # product price
            price_error = True
            while price_error:
                product_price = input('Price: [Ex: $4.55] ')     
                product_price = clean_price(product_price)
                if type(price_error) == int:
                    price_error = False
            
        
            
            # product quanity
            product_error = True
            while product_error:
                product_quantity = input('Quantity: ')
                product_quantity = clean_quantity(product_quantity)
                if type(product_quantity) == int:
                    price_error = False            
            
            # product data
            while date_error: 
                data_updated = input('Date: [Ex: 5/2/22')
                date_update = clean_date(data_updated)
                if type(date_update) == datetime.date:
                    date_error = False

        elif choice == 'b':
            # create backup
            pass 

        else:
            print('GOODBYE')
            app_running = False






if __name__ == '__main__':
     Base.metadata.create_all(engine)
    #  app()
    # clean_price('$4.55')

    


    

