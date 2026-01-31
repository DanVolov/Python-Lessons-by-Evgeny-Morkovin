import random
random_num = random.randint(1,100)
print('Добро пожаловать в числовую угадайку')

def is_valid(num, right):
    if not num.isdigit():
        return False
    num = int(num)
    return 1 <= num <= right


while True:
    count = 0
    r_border = input('Хотите указать правую границу числовой угадайки? Введите да или нет: ')
    if r_border.lower() == 'да':
        r_border_num = int(input('Введите число - правую границу числовой угадайки: '))
    else:
        r_border_num = 100

    random_num = random.randrange(1, r_border_num + 1)

    while True:
        n = input(f'Введите число от 1 до {r_border_num}: ')
        if is_valid(n, r_border_num):
            n = int(n)
            count += 1
            if n < random_num:
                print('Ваше число меньше загаданного, попробуйте еще разок')
            elif n > random_num:
                print('Ваше число больше загаданного, попробуйте еще разок')
            elif n == random_num:
                print('Вы угадали, поздравляем!')
                print(f'Количество попыток: {count}')
                break
        else:
            print(f'А может быть все-таки введем целое число от 1 до {r_border_num}?')
            continue

    a = input('Хотите сыграть ещё раз? Введите да или нет: ')
    if a.lower() != 'да':
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        break

'''
Задания:
Добавьте подсчет попыток, сделанных пользователем. Когда число отгадано, программа должна показать количество попыток;
Добавьте возможность генерации нового числа (повторная игра), после того, как пользователь угадал число;
Добавить возможность указания правой границы для случайного выбора числа (от 
1
1 до 
n
n).
'''
