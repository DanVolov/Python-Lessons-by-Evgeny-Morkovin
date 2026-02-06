from flask import Flask

from controllers import BookController, MemberController, OrdersController
from models import Book, Member, Orders

app = Flask(__name__)
book_controller = BookController()
member_controller = MemberController()
orders_controller = OrdersController()

@app.route('/')
def index():
    return book_controller.index()

@app.route('/delete/<id>')
def delete(id):
    return book_controller.delete(id)

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    return book_controller.edit(id)

@app.route('/add', methods=['GET', 'POST'])
def add():
    return book_controller.add()

@app.route('/search', methods=['GET', 'POST'])
def search():
    return book_controller.search()


@app.route('/members')
def members_index():
    return member_controller.index()

@app.route('/members/add', methods=['GET', 'POST'])
def members_add():
    return member_controller.add()

@app.route('/members/delete/<id>')
def members_delete(id):
    return member_controller.delete(id)

@app.route('/members/edit/<id>', methods=['GET', 'POST'])
def members_edit(id):
    return member_controller.edit(id)


@app.route('/orders')
def orders_index():
    return orders_controller.index()

@app.route('/orders/add', methods=['GET', 'POST'])
def orders_add():
    return orders_controller.add()

app.run(debug=True)