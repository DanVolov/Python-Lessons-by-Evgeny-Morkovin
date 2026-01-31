import sqlite3

def create_connection():
    try:
        conn = sqlite3.connect('library.db')
        return conn
    except Exception as e:
        print(f'{e}')
        return None


def create_table():
    conn = create_connection()
    sql1 = '''
    create table if not exists books(
        id integer primary key autoincrement,
        title text not null,
        author text not null,
        isbn integer not null,
        year integer not null,
        quantity integer default 1,
        available integer default 1
    )
    '''
    sql2 = '''
    create table if not exists members(
        id integer primary key autoincrement,
        name text not null,
        email text not null,
        phone text,
        join_date date default CURRENT_DATE
    )
    '''

    sql3 = '''
    create table if not exists orders(
        id integer primary key autoincrement,
        book_id integer not null,
        member_id integer not null,
        order_date date default CURRENT_DATE,
        foreign key (book_id) references books(id),
        foreign key (member_id) references members(id)
    )
    '''
    cursor = conn.cursor()
    try:
        cursor.execute(sql1)
        cursor.execute(sql2)
        cursor.execute(sql3)
        conn.commit()
        print('Таблица успешно создана')
    except Exception as e:
        print(f'{e}')

def test():
    conn = create_connection()
    book = [
        ('Название 1', 'Автор 1', '567', 2026, 5),
        ('Название 2', 'Автор 3', '568', 2026, 6),
        ('Название 3', 'Автор 3', '569', 2026, 157)
    ]
    member = [
        ('Иванов', 'tt@.com', '+764839'),
        ('Петров', 'tthnf@.com', '+76475839'),
        ('Сидоров', 'ttgnf@.com', '+7649867839')
    ]
    try:
        for i in book:
            cursor = conn.cursor()
            cursor.execute('insert into books (title, author, isbn, year, quantity) values (?, ?, ?, ?, ?)', i)
            #conn.commit()

        for i in member:
            cursor = conn.cursor()
            cursor.execute('insert into members (name, email, phone) values (?, ?, ?)', i)
            #conn.commit()
    except Exception as e:
        print(f'{e}')

create_table()
#test()