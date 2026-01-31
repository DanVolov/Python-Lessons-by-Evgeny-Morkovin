print('Добро пожаловать в программу для шифровки и дешифровки шифра Цезаря!')

action = input('Выберите действие (Шифровать или дешифровать): ')
language = input('Выберите язык (Русский или Английский): ')
step = int(input('Напишите сдвиг: '))
text = input('Напишите текст (в русском языке буква ё не учитывается): ')

if action.lower() == 'шифровать':
    if language.lower() == 'русский':
        result = ""

        for i in text:
            if 'А' <= i <= 'Я':
                result += chr((ord(i) - ord('А') + step) % 32 + ord('А'))
            elif 'а' <= i <= 'я':
                result += chr((ord(i) - ord('а') + step) % 32 + ord('а'))
            else:
                result += i

        print(result)

    elif language.lower() == 'английский':
        result = ""

        for i in text:
            if i.isalpha():
                base = ord('A') if i.isupper() else ord('a')
                shifted_char = chr((ord(i) - base + step) % 26 + base)
                result += shifted_char
            else:
                result += i

        print(result)

    else:
        print('Команда не распознана')

elif action.lower() == 'дешифровать':
    if language.lower() == 'русский':
        result = ""

        for i in text:
            if 'А' <= i <= 'Я':
                result += chr((ord(i) - ord('А') - step) % 32 + ord('А'))
            elif 'а' <= i <= 'я':
                result += chr((ord(i) - ord('а') - step) % 32 + ord('а'))
            else:
                result += i

        print(result)

    elif language.lower() == 'английский':
        result = ""

        for i in text:
            if 'A' <= i <= 'Z':
                result += chr((ord(i) - ord('A') - step) % 26 + ord('A'))
            elif 'a' <= i <= 'z':
                result += chr((ord(i) - ord('a') - step) % 26 + ord('a'))
            else:
                result += i

        print(result)

    else:
        print('Команда не распознана')

else:
    print('Команда не распознана')
