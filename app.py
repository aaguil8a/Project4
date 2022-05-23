from os import X_OK
from re import X
from types import new_class
from sqlalchemy.sql.expression import update
from models import Base, session, Product, engine
from menuhelper import *
from clean import *
import datetime
import csv
import time


def add_csv():
    with open('inventory.csv') as csvfile:
        data = csv.reader(csvfile)
        next(data)
        for row in data:
            product_in_db = (session.query(Product).filter(Product.product_name == row[0]).one_or_none())
            if product_in_db is None:
                product = row[0]
                price = clean_price(row[1])
                quantity = int(row[2])
                date = clean_date(row[3])
                new_product = Product(product_name=product, product_price=price, product_quantity=quantity, date_updated=date)
                session.add(new_product)
                
            elif product_in_db is not None:
                new_date = clean_date(row[3])
                product = (session.query(Product)
                           .filter(Product.product_name == row[0]).first())
                product.product_price = clean_price(row[1])
                product.product_quantity = int(row[2])
                product.date_updated = new_date

               
        session.commit()


def menu():
    while True:
        print('''
            \rPress [v] to view product details.
            \rPress [a] to add New Product.
            \rPress [b] to make a backup.csv.
            \rPress [q] to quit. ''')
        choice = input('What would you like to do? ').lower()
        if choice in ['v', 'a', 'b', 'q']:
            return choice
        else:
            input('Enter only the available options: (v, a, b, q)')


def app():
    app_running = True
    while app_running:
        choice = menu()
        if choice == 'v':
            get_productID()
        elif choice == 'a':
            add_product()
        elif choice == 'b':
            backup_csv()
        elif choice == 'q':
            print('Goodbye!')
            app_running = False


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    add_csv()
    app()
   
 
   