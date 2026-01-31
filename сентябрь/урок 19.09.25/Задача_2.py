'''
Задача 2: Анализ данных о студентах
У вас есть файл students.txt с информацией о студентах в формате: ID, имя, возраст, курс.
Требуется:
1.	Прочитать данные из файла.
2.	Сохранить данные в словарь, где ключом является ID, а значением — кортеж (имя, возраст, курс).
3.	Вывести список всех студентов, сгруппированных по курсу.
4.	Найти самого молодого и самого старшего студента
5.	Вычислить средний возраст студентов
6.	Найти студентов, которые учатся на двух и более курсах (если такие данные возможны)
7.	Вывести данные о студентах в новый файл
8.	Подсчет студентов в каждом курсе
9.	Найти студентов определенного возраста
10.	Перенос студентов определенного курса в другой файл
11.	Создать рейтинг студентов по возрасту в каждом курсе
12.	Определить наиболее популярный курс
13.	Добавление нового студента
'''
students = {}
with open('students.txt', 'r', encoding='utf-8') as f:
    d = f.readlines()
    for i in d:
        student = i.split(',')
        students[int(student[0])] = (student[1], int(student[2]), int(student[3].replace('\n', '')))
student_courses = {}
for i in students:
    if students[i][2] in student_courses:
        student_courses[students[i][2]].append((students[i][0], students[i][1]))
    else:
        student_courses[students[i][2]] = [(students[i][0], students[i][1])]

mx = 0
minx = 1000000000000000000000000000
name1 = ''
name2 = ''
for key in students:
    d = students[key]
    if d[1] > mx:
        mx = d[1]
        name1 = d[0]
    if d[1] < minx:
        minx = d[1]
        name2 = d[0]

print(mx, minx)
print(name1, name2)
print(students)
s = 0
for key in students:
    s += students[key][1]
print(int(s/len(students)))

print(round(1.41123123124, 2))

print(students)

with open('users_new.txt', 'w', encoding='utf-8') as f:
    for key in students:
        f.write(f'{key},{students[key][0]},{students[key][1]},{students[key][2]}\n')
