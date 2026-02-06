from flask import Flask, render_template, request, redirect, session, flash

from db import *
'''
куки (a=10, 24 часа)
сессии
'''

app = Flask(__name__)

app.secret_key = "3dfhgdfhdfjhokj436ghklhjl"
db()
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reg', methods=['GET', 'POST'])
def reg():
    print(session)
    if 'user_id' in session:
        return redirect('/')
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        email = request.form['email']

        user_id = add_user(login, password, email)
        if user_id:
            session['user_id'] = user_id
            session['login'] = login
            flash('Вы успешно вошли в систему', 'success')
        return redirect('/')

    return render_template('register.html')


@app.route('/auth', methods=['GET', 'POST'])
def auth():
    if 'user_id' in session:
        return redirect('/')
    if request.method == 'POST':
        login_auth = request.form.get('login_auth')
        password_auth = request.form.get('password_auth')
        
        user_id = auth_user(login_auth, password_auth)
        if user_id:
            session['user_id'] = user_id
            session['login'] = login_auth
            flash('Вы успешно вошли в систему', 'success')
            return redirect('/')
        else:
            flash('Неверный логин или пароль', 'error')
    
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user_id')
    session.pop('login')
    flash('Вы вышли из системы', 'info')
    return redirect('/')


@app.route('/catalog', methods=['GET', 'POST'])
def catalog():
    error = None
    if request.method == 'POST':
        if 'user_id' in session:
            id_product = request.form.get('id_product')
            quantity = request.form.get('quantity')
            id_user = session['user_id']
            add_product(id_product, quantity, id_user)
            return redirect('/cart')
        else:
            error = 'Для добавления товара необходимо пройти авторизацию!'
    products = select_products_all()

    product_list = []
    for product in products:
        product_list.append({
            'id': product[0],
            'name': product[1],
            'description': product[2],
            'price': product[3],
            'quantity': product[4],
            'image': product[5],
            'category': product[6]
        })

    return render_template('catalog.html', products=product_list, error=error)


@app.route('/cart', methods=['GET', 'POST'])
def cart():
    carts = None
    sum = 0
    if 'user_id' in session:
        if request.method == 'POST':
            id_product = request.form.get('id_product')
            delete_product_from_cart(id_product, session['user_id'])
            return redirect('/cart')
        carts = select_product_from_cart(session['user_id'])
        for summ in carts:
            sum += (summ[3] * summ[2])
    return render_template('cart.html', carts=carts, sum=sum)

@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        success = order_handler(session['user_id'])
        if success:
            flash('Заказ успешно оформлен!', 'success')
            return redirect('/')
        else:
            flash('Корзина пуста', 'error')

    return render_template('orders.html')

@app.route('/orders')
def orders():
    if not 'user_id' in session:
        return redirect('/')

    orders = select_orders(session['user_id'])


    return render_template('orders.html', orders=orders)


if __name__ == '__main__':
    app.run(debug=True,port=8000,host='0.0.0.0')

'''
написать ф-цию (db.py) которая очищает корзину авторизированного пользователя
обработчик заказа (/order) 
'''