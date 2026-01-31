#for while

i = 1
while i <= 10:
    print(i)
    i += 2


#10 9 8 7 6 5 4 3 2 1
i = 10
while i >= 1: #10 >= 1  9>= 1  1>=1  0>=1
    print(i)
    i -= 1

'''
while True:
    login = input('Login: ')
    password = input('Password: ')
    if login == 'admin' and password == 'admin':
        print('Login Successful')
    else:
        print('Login Failed')
        continue
    print('Login success')
'''
count = 0
for char in 'hello world':
    if char == ' ':
        count += 1
print(count)

'''
range(10) 0 1 2 3 4 5 6 7 8 9
range(5, 11) 5 6 7 8 9 10
range(1, 11, 2) 1 3 5 7 9
range(10, 0, -1)
'''

for i in range(100):
    print(i)
