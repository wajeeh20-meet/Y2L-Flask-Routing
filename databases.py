from model import Base, Product, Cart


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def add_product(name, price, picturelink,description):
   
    product_object = Product(
        name=name,
        price=price,
        picturelink=picturelink,
        description = description)
    session.add(product_object)
    session.commit()


def edit_by_id(id, name):
  
   price_object = session.query(
       Product).filter_by(
       name=name).first()
   price_object.name = name
   session.commit()




def delete_product(its_name):
   
   session.query(Product).filter_by(
       name=its_name).delete()
   session.commit()




def query_all():
  
   products = session.query(
      Product).all()
   return products


def query_by_name(its_name):
  
   product = session.query(
       Product).filter_by(
       name=its_name).first()
   return product


def query_by_id(id):
  
   product = session.query(
       Product).filter_by(
       id=id).first()
   return product


def Add_To_Cart(productID):
  cart_object = Cart(productID = productID)
  session.add(cart_object)
  session.commit()
   
def query_all_cart():
  
   carts = session.query(
      Cart).all()
   return carts








# add_product("wael's jacket", 2, "/static/wael.jpg", "george's camera!!")

