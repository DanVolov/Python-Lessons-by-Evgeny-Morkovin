import sqlite3
from database import create_connection


class Book:
    def __init__(self, title=None, author=None, isbn=None, year=None, quantity=1, available=1):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.quantity = quantity
        self.available = available
        self.connection = create_connection()
        self.cursor = self.connection.cursor()

    def get_all(self):
        self.cursor.execute("SELECT * FROM books")
        return self.cursor.fetchall()

    def get_by_id(self, id):
        self.cursor.execute("SELECT * FROM books WHERE id=?", (id,))
        return self.cursor.fetchone()

    def add(self, title, author, isbn, year, quantity):
        self.cursor.execute("insert into books (title, author, isbn, year, quantity) values (?, ?, ?, ?, ?)", (title, author, isbn, year, quantity))
        self.connection.commit()

    def update(self, id, title, author, isbn, year, quantity):
        self.cursor.execute('update books set title = ?, author=?,isbn=?, year=?,quantity=? where id=?', (title, author, isbn, year, quantity, id))
        self.connection.commit()

    def delete(self, id):
        self.cursor.execute('delete from books where id=?', (id,))
        self.connection.commit()

    def search(self, query):
        self.cursor.execute('select * from books where title like ? or author like ?', (query, query))
        return self.cursor.fetchall()


class Member:
    def __init__(self, id, name, email, phone):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone

        self.connection = create_connection()
        self.cursor = self.connection.cursor()

    def get_all(self):
        self.cursor.execute("SELECT * FROM members")
        return self.cursor.fetchall()

    def get_by_id(self, id):
        self.cursor.execute("SELECT * FROM members WHERE id=?", (id,))
        return self.cursor.fetchone()

    def add(self, name, email, phone):
        self.cursor.execute("insert into members (name, email, phone) values (?, ?, ?)", (name, email, phone))
        self.connection.commit()

    def update(self, id, name, email, phone):
        self.cursor.execute('update members set name = ?, email=?, phone=? where id=?', (name, email, phone, id))
        self.connection.commit()

    def delete(self, id):
        self.cursor.execute('delete from members where id=?', (id,))
        self.connection.commit()


class Orders:
    def __init__(self):
        self.connection = create_connection()
        self.cursor = self.connection.cursor()

    def order_book(self, book_id, member_id):
        self.cursor.execute('select available from books where book_id=?', (book_id,))
        if self.cursor.fetcone()[0] > 0:
            self.cursor.execute('update books set available = available - 1 where id=?', (book_id,))
            self.cursor.execute('insert into orders (book_id, member_id) values (?, ?)', (book_id, member_id))
            self.connection.commit()
            success = True
        else:
            success = False
        return success


