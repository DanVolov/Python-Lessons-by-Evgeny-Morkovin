from flask import render_template
from shop import create_app


app = create_app()
@app.route('/')
def home():
    from shop.models.product import Product
    #products = Product.query.all()
    return render_template('home.html')


app.run(debug=True)
