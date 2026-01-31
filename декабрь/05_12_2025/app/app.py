from flask import Flask, request, redirect, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/reg', methods=['GET', 'POST'])
def reg():
    if request.method == 'POST':
        #обработчик страницы регистрации
        form = request.form
        login = form.get('login')
        password = form.get('password')
        email = form.get('email')
        with open('users.txt', 'a', encoding='utf-8') as f:
            f.write(f'{login}:{password}:{email}\n')
        return redirect('/login')
    else:
        #когда заходим на страницу регистрации
        return render_template('reg.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    s = False
    if request.method == 'POST':
        #обработчик страницы авторизации
        form = request.form
        login = form.get('login')
        password = form.get('password')
        if login == 'admin' and password == 'admin':
            s = True
    return render_template('login.html', s=s)


app.run(debug=True)