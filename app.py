from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from databases import *

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


##### Code here ######
@app.route("/")
def home():
	return render_template("home.html")



@app.route("/store")
def store():
	products = query_all()
	# for product in products:
	# 	print(product.name)
	return render_template("store.html", Products = products)


@app.route("/cart")
def cart():
	carts = query_all_cart()
	
	return render_template("cart.html", carts=carts)


@app.route("/about")
def about():
	return render_template("about.html")



#####################


if __name__ == '__main__':
    app.run(debug=True)