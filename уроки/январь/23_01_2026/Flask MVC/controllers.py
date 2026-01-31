from flask import  render_template, request, redirect
from models import Book, Member, Orders

class BookController:
    def index(self):
        book = Book()
        books = book.get_all()
        return render_template('books.html', books=books)
    def add(self):
        if request.method == 'POST':
            title = request.form['title']
            author = request.form['author']
            isbn = request.form['isbn']
            quantity = int(request.form['quantity'])
            year = request.form['year']
            book = Book(title, author, isbn, year, quantity)
            book.add(title, author, isbn, year, quantity)
            return redirect('/')
        else:
            return render_template('add.html')
    def delete(self, id):
        book = Book()
        book.delete(id)
        return redirect('/')
    def edit(self, id):
        if request.method == 'POST':
            title = request.form['title']
            author = request.form['author']
            isbn = request.form['isbn']
            quantity = int(request.form['quantity'])
            year = request.form['year']
            book = Book()
            book.update(id, title, author, isbn, year, quantity)
            return redirect('/')
        else:
            book = Book()
            book = book.get_by_id(id)
            return render_template('edit.html', book=book)

    def search(self):
        if request.method == 'POST':
            query = request.form['query']
            book = Book()
            books = book.search(query)
            return render_template('books.html',  books=books)
        else:
            return render_template('searchbook.html')
    #edit, search