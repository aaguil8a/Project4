from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///inventory.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Product(Base):
    __tablename__ = 'products'

    product_id = Column(Integer, primary_key=True)
    product_name = Column(String) 
    product_quantity = Column(Integer)
    product_price = Column(Integer)
    date_updated = Column(DateTime)

    def __repr__(self):
        print('f Product name {self.product_name}, Quantity: {self.proquantity}, Price: {self.product_price}, Update: {self.date_updated}')