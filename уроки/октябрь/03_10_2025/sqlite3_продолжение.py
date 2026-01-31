import sqlite3


'''
выборка данных из БД
'''
conn = sqlite3.connect('интернет_магазин.db')
c = conn.cursor()
c.execute('select * from products')
products = c.fetchall()
for i in products:
    #print(i[1], i[2], 'руб.')
    print(f'{i[1]} {i[2]} руб.')



c.execute('select * from orders')
orders = c.fetchall()
summa = 0
for j in orders:
    summa = summa + j[1]

print(summa)


c.execute('select * from users')
users = c.fetchall()
for a in users:
    print(a[1], a[2])

'''
Удаление данных в БД
'''

c.execute('delete from products where price > 40000')
conn.commit()

