import sqlite3
conn = sqlite3.connect('интернет_магазин.db')
c = conn.cursor()
c.execute('delete from products where price > 20000')
conn.commit()

#обновление
c.execute('update products set price = 30000 where id = 4')
conn.commit()

c.execute('insert into products (name, price, category) values ("product 1", 222, "cat 1")')
conn.commit()
print(1)