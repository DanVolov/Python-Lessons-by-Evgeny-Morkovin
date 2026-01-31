'''
1.	Введите строку, содержащую числа в виде слов, и
преобразуйте их в числовую форму (например, "один два три" → 1 2 3).
'''
s = "три один два три"
a = s.split(' ')
h = {'один': 1, 'два': 2, 'три': 3}
#print(h['три'])
l = []
for i in a:
    l.append(str(h[i]))
print(l)
print(' '.join(l))

'''
2.	Напишите программу, которая принимает URL и извлекает домен из него.
https://docs.python.org/3/library/urllib.html
'''
url = 'https://docs.python.org/3/library/urllib.html'
a = url.split('/')
print(a[2])

'''
3.	Введите строку и замените каждое второе слово в ней на слово "Python"
'''

str = "hello world hellow world str"

a = str.split(' ')
'''
['hello', 'world', 'hellow', 'world', 'str']
  0          1          2       3       4
'''
for i in range(0, len(a)-1):
    if i % 2 == 1:
        a[i] = "python"

print(a)

'''
4.	Напишите программу, которая извлекает все числа из строки.

'sfasf 24124 asfasf23523dfg' -> 2412423523
'''

a = 'sfasf 24124 asfasf23523dfg'

b = ""

for i in a:
    if i.isdigit():
        print(i)
        b = b + i
print(b)

'''
5.	Напишите программу, которая парсит строку с математическим выражением 
(например, 3 + 4 * 2 / (1 - 5)) и вычисляет результат с учётом приоритета операций
'''

f = '3 + 4 * 2 / (1 - 5)'
print(eval(f))

'''
6.	Напишите программу, которая преобразует строку в формат заголовка (например, "hello world" → "Hello World").
'''

str = 'hello world'
print(str.title())

'''
7.	Напишите программу, которая извлекает имя пользователя из строки email-адреса 
(например, "user@example.com" → "user").
'''

mail = 'user@example.com'

a = mail.split('@')

print(a[0])

#файлы, ООП, модули
#