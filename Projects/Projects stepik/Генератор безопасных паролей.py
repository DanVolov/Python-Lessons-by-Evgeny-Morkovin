from random import choice

DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'

chars = ''

cntPw = int(input('Укажите количество паролей для генерации: '))
lenPw = int(input('Укажите длину одного пароля: '))
digOn = input('Включать ли цифры 0123456789? (y/n): ')
ABCon = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n): ')
abcOn = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n): ')
chOn = input('Включать ли символы !#$%&*+-=?@^_? (y/n): ')
excOn = input('Исключать ли неоднозначные символы il1Lo0O? (y/n): ')

if digOn == 'y':
    chars += DIGITS

if ABCon == 'y':
    chars += UPPERCASE_LETTERS

if abcOn == 'y':
    chars += LOWERCASE_LETTERS

if chOn == 'y':
    chars += PUNCTUATION

if excOn == 'y':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')

def generate_password(length, chars):
    password = ''
    for _ in range(length):
        password += choice(chars)
    return password
        
while cntPw != 0:
    print(generate_password(lenPw, chars))
    cntPw -= 1
