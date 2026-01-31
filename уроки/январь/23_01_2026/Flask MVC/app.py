from flask import Flask

from controllers import BookController
from models import Book, Member, Orders

app = Flask(__name__)
controller = BookController()

@app.route('/')
def index():
    return controller.index()

@app.route('/delete/<id>')
def delete(id):
    return controller.delete(id)

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    return controller.edit(id)

@app.route('/add', methods=['GET', 'POST'])
def add():
    return controller.add()

@app.route('/search', methods=['GET', 'POST'])
def search():
    return controller.search()
#CRUD

app.run(debug=True)