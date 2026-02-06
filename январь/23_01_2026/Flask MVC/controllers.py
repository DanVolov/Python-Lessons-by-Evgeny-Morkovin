from flask import render_template, request, redirect
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
            return render_template('books.html', books=books)
        else:
            return render_template('searchbook.html')


class MemberController:
    def index(self):
        member = Member()
        members = member.get_all()
        return render_template('members.html', members=members)

    def add(self):
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            phone = request.form.get('phone', '')
            member = Member()
            member.add(name, email, phone)
            return redirect('/members')
        return render_template('add_member.html')

    def delete(self, id):
        member = Member()
        member.delete(id)
        return redirect('/members')

    def edit(self, id):
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            phone = request.form.get('phone', '')
            member = Member()
            member.update(id, name, email, phone)
            return redirect('/members')
        member = Member()
        m = member.get_by_id(id)
        return render_template('edit_member.html', member=m)


class OrdersController:
    def index(self):
        orders_model = Orders()
        orders = orders_model.get_all()
        return render_template('orders.html', orders=orders)

    def add(self):
        book = Book()
        member = Member()
        books = book.get_all()
        members = member.get_all()
        if request.method == 'POST':
            book_id = int(request.form['book_id'])
            member_id = int(request.form['member_id'])
            orders_model = Orders()
            if orders_model.add(book_id, member_id):
                return redirect('/orders')
            return render_template('add_order.html', books=books, members=members)
        return render_template('add_order.html', books=books, members=members)

    def get_by_id(self, id):
        orders_model = Orders()
        order = orders_model.get_by_id(id)
        return render_template('orders.html', order=order)