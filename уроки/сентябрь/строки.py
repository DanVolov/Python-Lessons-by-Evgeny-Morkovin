m = 'hello'
h1 = "hello"
c = 1
print(type(c))
d = '''
asf
asf
as
fas
fasfasfa as fasfas
fa
sf
asfas fas fa
'''
print(d)

m1 = 'he\tllo\nworld'
print(m1)

h = "asfas as fasf as f\" asfasfasf"
print(h)

name = 'User'
age = 34
user = f'Name: {name} Age: {age}'
user1 = "Name: " + name + " Age: " + str(age)
print(user)
print(user1)

s = 'string'
print(s[0])
print(s[-1])
print(s[0:3])
print(s[0:5:2])
print(s[::-1])

print('hello' * 30)
print(ord('a'))
print(ord('b'))
print('a' > 'b') #97 > 98
print(len('abcd'))
print('hello' not in 'sdfa as fasf asfhello afasfasf')

'''
методы
'''
s = 'JKSHFJSF'
print(s.isalpha())
print(s.isdigit())
print(s.islower())
print(s.isupper())
print(s.startswith('JKl'))
print(s.endswith('SHF'))

print(s.lower())
print(s.upper())

s = '     hello world'
print(s.title())
print(s.capitalize())
print(s.strip())


s = 'hello world'
print('world' in s)
print(s.find('world'))
s = 'hello world hello world'
print(s.replace('world', '***'))

c = ['1', '2', '3']
print('.'.join(c))



'''
на длину пароля > 8
1 символ сточный и заглавный
1 символ цифра 
'''
password = input("Введите пароль: ")

if len(password) > 8:
    m1 = False
    for char in password:
        if char.islower():
            m1 = True
            break
    m2 = False
    for i in password:
        if i.isupper():
            m2 = True
            break
    m3 = False
    for a in password:
        if a.isdigit():
            m3 = True
            break
    if m1 and m2 and m3:
        print("True")
    if m1 == False:
        print("False m1")
    if m2 == False:
        print("False m2")
    if m3 == False:
        print("False m3")
else:
    print("error")

'''
f''
format()
'''
name = 'User'
age = 33
info = 'Name: {name} Age: {age}'.format(name=name, age=age)
print(info)