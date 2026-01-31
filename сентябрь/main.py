import math

print('hello world', end='\t')
print("hello world")
print((10 + 20) - 4 * 5 / 5)
print(11 // 4) #2
print(11 % 4) #3
print(11 ** 3)
print(64 ** (1/2))
print(math.sqrt(64))
print(math.pi)
print(math.pow(3,4))

a = int(input('a=')) #str
'''
int -1 1 10
float 1.0 4.0003
str '' ""
bool True False
'''
f = 1
print(bool(f)) #True
print(bool('')) #False

'''
==
!=
>
<
>=
<=
'''
a = 1
b = 2
if a == b:
    print('true')
else:
    print('false')

'''
булевые операции
and not or
False and False -> False
True and False -> False
False and True -> False
True and True -> True
'''

login = input('Login: ')
if login and len(login) >= 3:
    password = input('Password: ')
    if password == login:
        print('Login Success')
    else:
        print('Login Failed')
else:
    print('Login Failed')




