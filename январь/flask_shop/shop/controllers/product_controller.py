from shop.models import Product
from flask import request, render_template

from уроки.январь.shop.models.product import Category


class ProductController:

    @staticmethod
    def list_products():
        page = request.args.get('page', 1, type=int)
        category_id = request.args.get('category_id', type=int)
        search = request.args.get('search', '')
        query = Product
        if category_id:
            query = query.filter_by(category_id = category_id)
        if search:
            query = query.filter(Product.name.ilike(f'%{search}%'))

        products = query.paginate(page=page, per_page=12, error_out=False)
        categories = Category.query.all()

        return render_template('product/product_list.html', products=products, categories=categories, search=search, category_id=category_id)


    @staticmethod
    def product_detail(product_id):
        product = Product.query.get_or_404(product_id)

        similar_products = Product.query.filter(Product.category_id == product.category_id).limit(4).all()
        return render_template('product/product_detail.html', product=product, similar_products=similar_products)
