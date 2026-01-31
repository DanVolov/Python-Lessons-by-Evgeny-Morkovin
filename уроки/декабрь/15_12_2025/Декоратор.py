import time
from functools import wraps
def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        end = time.time()
        result = func(*args, **kwargs)
        print(end-start)
        print(func.__name__)
        print(args, kwargs)
        return result
    return wrapper

@log_call
def test(a, b):
    return a * b

print(test(3, 2))


'''
Декоратор для логирования
Напишите декоратор log_call, который записывает в файл:

Время вызова функции

Имя функции

Аргументы функции

Возвращаемое значение
'''