import sqlite3
'''
postgresql - cервер
mysql - сервер
sqlite3 - файл с БД
База данных состоит из таблиц

Пример БД "Интернет-магазина"
Products(Товары)
id   name       price    category
1    Смартфон 1 22222    Смартфоны
2    Смартфон 2 65567    Смартфоны

Orders(Заказы)
id   summa   products   date_d  
1    345234  1,2        26.09.2025 10:00 
2    235235  2          28.09.2025 10:00 

Users(ПОльзователи)
id   login  password email           phone balance
1    user1  12345    admin@admin.ru 235235 0

Basket
id product_id count summa


подключаемс к БД
и делаем запросы (регистрация пользователя (добавление данных), изменение статуса (обновление данных), удаление пользователя (удаление), выбор товаров (выборка))
добавление
обновление
удаление
выборка
'''


conn = sqlite3.connect('интернет_магазин.db')
cursor = conn.cursor()
cursor.execute('''
create table if not exists products(
id integer primary key autoincrement,
name varchar(255),
price text,
category text
)
''')

cursor.execute('''
create table if not exists orders(
id integer primary key autoincrement,
summa int,
products text,
date_order date
)
''')

cursor.execute('''
create table if not exists users(
id integer primary key autoincrement,
login text,
password text,
email text,
phone text,
balance int
)
''')

products = [
    {'name': 'Товар 1', 'price': 22222, 'category': 'Категория 1'},
    {'name': 'Товар 2', 'price': 45, 'category': 'Категория 1'},
    {'name': 'Товар 3', 'price': 223222, 'category': 'Категория 1'},
    {'name': 'Товар 4', 'price': 12222, 'category': 'Категория 1'},
    {'name': 'Товар 5', 'price': 32222, 'category': 'Категория 1'},
    {'name': 'Товар 6', 'price': 42222, 'category': 'Категория 2'},
    {'name': 'Товар 7', 'price': 52222, 'category': 'Категория 2'},
    {'name': 'Товар 8', 'price': 22222, 'category': 'Категория 2'},
    {'name': 'Товар 10', 'price': 42222, 'category': 'Категория 2'},
]


for product in products:
    '''
    добавление данных в БД
    '''
    cursor.execute('insert into products (name, price, category) values (?, ?, ?)', (product['name'], product['price'], product['category']))
    conn.commit()

'''
insert into products (name, price, category) values ('Товар 1', 235235, 'Категория 1'))
'''

users = [
    {'login': 'user1', 'password': '12345', 'email': '', 'phone': '0123456789', 'balance': 22222},
    {'login': 'user2', 'password': '12345', 'email': '', 'phone': '0123456789', 'balance': 22222},
    {'login': 'user3', 'password': '12345', 'email': '', 'phone': '0123456789', 'balance': 22222},
]
for user in users:
    '''
    добавление данных в БД
    '''
    cursor.execute('insert into users (login, password, email, phone, balance) values (?, ?, ?, ?, ?)', (user['login'], user['password'], user['email'], user['phone'], user['balance']))
    conn.commit()

#ДЗ добавить 10 заказов со случайными данными

orders = [
    {'summa': 542354, 'products': 'Телефон', 'date_order': '02.10.2025'},
    {'summa': 45533, 'products': 'Телефон', 'date_order':  '01.10.2025'},
    {'summa': 43534, 'products': 'Телефон', 'date_order': '30.09.2025'},
    {'summa': 1243, 'products': 'Одежда', 'date_order': '29.09.2025'},
    {'summa': 1644, 'products': 'Одежда', 'date_order': '28.09.2025'},
    {'summa': 536, 'products': 'Одежда', 'date_order': '27.09.2025'},
    {'summa': 43245, 'products': 'Телефон', 'date_order': '26.09.2025'},
    {'summa': 13657, 'products': 'Мебель', 'date_order': '25.09.2025'},
    {'summa': 95037, 'products': 'Телефон', 'date_order': '24.09.2025',},
    {'summa': 25357, 'products': 'Мебель', 'date_order': '23.09.2025', }
]

for order in orders:
    cursor.execute('insert into orders (summa, products, date_order) values (?, ?, ?)', (order['summa'], order['products'], order['date_order']))
    conn.commit()