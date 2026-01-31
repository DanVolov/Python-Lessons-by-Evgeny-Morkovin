import sqlite3
conn = sqlite3.connect('интернет_магазин.db')
c = conn.cursor()
auth = False
id_user = None
while True:
    if auth:
        mode_profile = int(input('1 - Ваш профиль 2 - Выход 3 - список закаов'))
        if mode_profile == 1:
            c.execute('select * from users where id = ?', (id_user,))
            user = c.fetchone()
            print(f'login: {user[1]}, password: {user[2]}, email: {user[3]}, telephone: {user[4]}, balance: {user[5]}')
            login_new = input('new login:')
            password_new = input('new password:')
            email_new = input('new email:')
            telephone_new = input('new telephone:')

            c.execute('update users set login = ?, password = ?, email = ?, phone = ? where id = ?', (login_new, password_new, email_new, telephone_new, id_user))
            conn.commit()
            print('Данные успешно обновлены')
        elif mode_profile == 2:
            auth = False
        elif mode_profile == 3:
            c.execute('select * from orders where id_user = ?', (id_user,))
            orders = c.fetchall()
            k = 1
            for b in orders:
                print(f'{k}. summa: {b[1]}, date: {b[3]}')
                k += 1
            sum = 0
            for d in orders:
                sum = sum + d[1]

            print(f'total: {sum}')
    else:
        mode = int(input('1 - Регистрация 2 - Авторизация '))
        if mode == 1:
            login = input('login: ')
            if len(login) >= 3 and len(login) != 0:
                password = input('password: ')
                if len(password) >= 8:
                    m = False
                    for i in password: #jj11sdfgkjasdgkldsg
                        if i.isdigit():
                            m = True
                            break

                    if not m:
                        print('Error password digit')
                        continue
                    #регулярные выражения
                    email = input('email: ')
                    telephone = input('telephone: ') #+7(111)222-22-22
                    balance = 0
                    c.execute('insert into users (login, password, email, phone, balance) values (?, ?, ?, ?, ?)', (login, password, email, telephone, balance))
                    conn.commit()
                    print('ok')
                else:
                    print('Error password')
                    continue
            else:
                continue
        elif mode == 2:
            login = input('login: ')
            password = input('password: ')
            c.execute('select * from users where login = ? and password = ?', (login, password))
            f = c.fetchone()
            '''
            fetchall() [(1,1,1,1,1)]  [0][0]
            fetchone() (1,1,1,1,1) [0]
            '''

            if f:
                auth = True
                print('Вы успешно прошли авторизацию')
                id_user = f[0]