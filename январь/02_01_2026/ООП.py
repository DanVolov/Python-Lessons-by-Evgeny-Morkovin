'''
класс - некоторая сущность
обьект - конкретное вопрощение класса

class название_класса:
    атрибуты_класса(имя,возраст)
    методы_класса(ходить, думать)
'''

class Person:

    #конструктор
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #метод
    def info(self):
        return f'Меня зовут {self.name}, мне {self.age} лет'



user1 = Person('Вася', 16) #создание обьекта
user2 = Person('Петя', 18) #создание обьекта

print(user1.name, user1.age)
print(user2.name, user2.age)
user1.age = 18
print(user1.name, user1.age)
print(user1.info())
print(user2.info())





'''
основные концепции ООП
1. Классы и обьекты
2. Инкапсуляция (сокрытие внутренней реализации)
'''

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance #__приватный атрибут, доступен только внутри класса


    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def get_balance(self):
        return self.__balance


b1 = BankAccount('Иван', 1000)
b2 = BankAccount('Вася', 2000)

print(b1.deposit(1000))
print(b1.withdraw(2000000))
print(b1.get_balance())


print('#' * 10)

class Student:
    def __init__(self, name, age, grades):
        self.__name = name
        self.__age = age
        self.__grades = grades

    def add_grade(self, grade):
        if 0 <= grade <= 10:
            self.__grades.append(grade)

    def info_grades(self):
        return self.__grades

    def grade_point_average(self):
        count = len(self.__grades)
        sum = 0
        for grade in self.__grades:
            sum += grade

        return sum / count

student1 = Student('Alex', 20, [5, 6, 8])
student2 = Student('John', 23, [10, 6, 3, 1, 7])

student1.add_grade(10)
print(student1.info_grades())
print(student1.grade_point_average())

student2.add_grade(20)
student2.add_grade(-5)
print(student2.info_grades())
print(student2.grade_point_average())

student3 = Student('Boris', 21, [3, 6, 1, 10])
student3.add_grade(10)
print(student3.info_grades())
print(student3.grade_point_average())

'''
Создать класс Студент, который хранит: приватные атрибуты для имени, возраста и оценок
Оценки должны быть в диапазоне 0-10
методы для добавления и получения оценок
метод для вычисления ср. балла
'''