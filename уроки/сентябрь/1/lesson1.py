'''


1. Открываем файл в указанному режиме ('r', 'w', 'a')
r (read) - чтение
w (write) - Добавить
a (append) - добавление в конце файла
2. Что то делаем с файлом
3. Закрываем файл

абсолютная адресация - d:/1/2/1.txt
относительная - users.txt
'''
'''
f = open('users.txt', 'r')

d = f.read() # в скобках байты указывать
d = f.readline() # первая строка

d = f.readlines() # преобразует в список
for in in d;
    print(i.replace('\n', ''))
f.close()
'''
'''
f = open('users.txt', 'w', encoding='utf-8') #utf-8 и для русских
f.write("Привет") # написать что то в файл
f.close()
'''
'''
f = open('users.txt', 'a', encoding='utf-8')
f.write('\nПривет мир')
f.close()
'''

#Контекстный мессенджер

'''
with open('users.txt', 'w', encoding='utf-8') as f:
    f.write("12345")
'''

