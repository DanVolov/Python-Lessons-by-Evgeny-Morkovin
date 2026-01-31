#print(10 / 0)
'''
ZeroDivisionError
TypeError
IndexError
KeyError
ImportError
ValueError

print(str(10) + '10')
a = [1,2,3]
#print(a[5])
b = {'a': 1, 'b': 2}
print(b['c'])

print(1)
print(2)



while True:
    try:
        age = int(input())
        print(10 / 0)
    except ValueError:
        print('Error')
    except ZeroDivisionError:
        print('Error')



while True:
    login = input('Login: ')
    password = input('Password: ')
    try:
        if login == password:
            raise ValueError('Логин и пароль не должны совпадать')
    except ValueError as e:
        print(e)


try:
    a = 10
    b = 20
    print(a / 0)
except:
    print('Error')
finally:
    print('Ok')
'''