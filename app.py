from audioop import add
from models import (Base, Product, engine)
# import datatime
import csv


def add_csv():
    with open('inventory.csv') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            print(row)


if __name__ == '__main__':
    # Base.metadata.create_all(engine)
    add_csv()


