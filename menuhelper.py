from clean import *
from sqlalchemy.sql.expression import update
from models import Base, session, Product, engine
import datetime
import csv
import time


def get_productID():
    id_options = []
    for product in session.query(Product):
        id_options.append(product.product_id)
    id_error = True
    while id_error:
        id_choice = input('\n Enter product number: ')
        id_choice = clean_id(id_choice, id_options)
        if type(id_choice) == int:
            id_error = False
    the_product = (session.query(Product).filter(Product.product_id == id_choice).first())
    print(f'''
        \n{the_product.product_name}: 
        \rQuantity: {the_product.product_quantity}
        \rPrice: ${the_product.product_price/100} 
        \rDate updated: {the_product.date_updated}''') 
    time.sleep(1.5)


def add_product():
    product = input('Enter the product: ')

    price_error = True
    while price_error:
        price = clean_price(input('Price: Ex., $5.51: '))
        if type(price) == int:
            price_error = False

    quantity_error = True
    while quantity_error:
        try:
            quantity = int(input('Quantity: Ex., 56: '))
            quantity_error = False
        except ValueError:
            input('''
                \n***** QUANTITY ERROR *****
                \rThe quantity should be a number: Ex., 56
                \rPress [ENTER] to try again.''')
    date_error = True
    while date_error:
        date = clean_date(input("Date: ex. 5/19/2022)"))
        if type(date) == datetime.date:
            date_error = False
    time.sleep(1.5)

def backup_csv():
    print('New database filename is backup.csv')
    time.sleep(1.5)
    with open('backup.csv', 'w', newline='') as csvfile:
        column_names = ['product_name', 'product_price', 'product_quantity','date_updated']
        writer = csv.DictWriter(csvfile,delimiter=',',fieldnames=column_names) 
        writer.writeheader()
        for product in session.query(Product):
            writer.writerow({
                'product_name': product.product_name,
                'product_price': product.product_price,
                'product_quantity': product.product_quantity,
                'date_updated': product.date_updated
            })

    print('Backup created!')
    time.sleep(1.5)
       