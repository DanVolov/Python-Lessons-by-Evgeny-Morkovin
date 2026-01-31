import sqlite3

def db():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute('''
    create table if not exists users (
        id integer primary key autoincrement,
        login text not null,
        password text not null,
        email text not null
    )
    ''')

    c.execute('''
    create table if not exists products (
        id integer primary key autoincrement,
        name text not null,
        description text not null,
        price integer not null,
        quantity integer not null,
        image text not null,
        category text not null
    )
    ''')

    c.execute('''
    create table if not exists cart(
        id integer primary key autoincrement,
        product_id integer not null,
        quantity integer not null,
        user_id integer not null,
        foreign key (user_id) references users(id),
        foreign key (product_id) references products(id)
    )
    ''')

    c.execute('''
        create table if not exists orders(
            id integer primary key autoincrement,
            total_summa integer not null,
            user_id integer not null,
            foreign key (user_id) references users(id)
        )
        ''')
    conn.commit()
    '''
    c.execute('DELETE FROM products')
    conn.commit()

    name_list = [
        "Футболка",
        "Настольная лампа",
        "Беспроводные наушники",
        "Кухонный таймер",
        "Чемодан на колёсиках",
        "Горшок для цветов",
        "Электрический чайник",
        "Игровая компьютерная мышь",
        "Ёмкость для хранения",
        "Коврик для йоги"
    ]

    for _ in range(10):
        name = random.choice(name_list)
        description = name
        price = random.randint(1, 10000)
        quantity = random.randint(1, 10)
        image = ''

        if name == 'Футболка':
            category = 'Одежда'
        elif name in ['Настольная лампа', 'Беспроводные наушники', 'Кухонный таймер', 'Электрический чайник', 'Игровая компьютерная мышь']:
            category = 'Электроника'
        elif name in ['Чемодан на колёсиках', 'Горшок для цветов', 'Ёмкость для хранения', 'Коврик для йоги']:
            category = 'Другое'
        else:
            category = 'Неизвестно'

        c.execute(
            'INSERT INTO products (name, description, price, quantity, image, category) VALUES (?, ?, ?, ?, ?, ?)',
            (name, description, price, quantity, image, category))

    conn.commit()
    conn.close()
    '''
def add_user(login, password, email):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    try:
        c.execute('insert into users (login,password,email) values (?,?,?)', (login, password, email))
        conn.commit()
        user_id = c.lastrowid
        return user_id
    except:
        return None
    finally:
        conn.close()

def auth_user(login, password):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute('select id from users where login=? and password=?', (login, password))
    user = c.fetchone()
    conn.close()
    if user:
        return user[0]
    return None

def add_product(id_product, quantity, id_user):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute('insert into cart (product_id, quantity, user_id) values (?, ?, ?)', (id_product, quantity, id_user))
    conn.commit()


def select_products_all():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute('SELECT * FROM products')
    return c.fetchall()

def select_product_from_cart(id_user):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute('SELECT c.product_id, p.name, sum(c.quantity), p.price FROM cart c join products p on c.product_id=p.id  WHERE c.user_id=? group by c.product_id,p.name,p.price', (id_user,))
    return c.fetchall()

def delete_product_from_cart(id_product, user_id):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute('DELETE FROM cart WHERE product_id=? and user_id = ? ', (id_product,user_id))
    conn.commit()

def order_handler(user_id):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute('SELECT SUM(c.quantity * p.price) FROM cart c JOIN products p ON c.product_id = p.id WHERE c.user_id = ?', (user_id,))

    total_summa = c.fetchone()[0]

    if total_summa is None:
        conn.close()
        return False

    c.execute('INSERT INTO orders (total_summa, user_id) VALUES (?, ?)',(total_summa, user_id))
    c.execute('DELETE FROM cart WHERE user_id = ?', (user_id,))

    conn.commit()
    conn.close()
    return True

def select_orders(user_id):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute('SELECT * FROM orders WHERE user_id = ?', (user_id,))
    return c.fetchall()

'''
users
id login password
1  user1 12345
2  user2 12345

products
id name   price
1  товар1 3333
2  товар2 555

cart
id user_id product_id
1  1        2
'''