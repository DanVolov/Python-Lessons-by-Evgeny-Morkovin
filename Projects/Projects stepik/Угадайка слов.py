import random

word_list = ['пастель', 'акварель', 'пейзаж', 'натюрморт', 'рассвет', 'горизонт', 'фреска', 'мозаика', 'иней', 'этюд']
art = [word_list[0], word_list[1], word_list[2], word_list[3], word_list[6], word_list[7], word_list[9]]
nature = [word_list[4], word_list[5], word_list[8]]


def get_word():
    return random.choice(word_list).upper()

def is_valid(word_input):
    if word_input.isalpha() and len(word_input) == 1:
        return True
    else:
        return False

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


def play(word):
    word_completion = '_' * len(word)
    guessed = False
    guessed_letters = []
    tries = 6
    word_as_list = list(word_completion)
    hint_used = False
    hint_used_category = False

    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))
    print(word_completion)

    while not guessed and tries > 0:
        if not hint_used:
            add_question = input('Подсказка! Хотите узнать первую и последнюю букву слова? (да/нет): ')
            if add_question.lower() == 'да':
                word_as_list[0] = word[0]
                word_as_list[-1] = word[-1]
                word_completion = ''.join(word_as_list)
                hint_used = True
                print(word_completion)
                print("Вы использовали подсказку!")

        if not hint_used_category:
            add_question_category = input('Подсказка! Хотите узнать, к какой категории относится слово? (да/нет): ')
            if add_question_category.lower() == 'да':
                if word.lower() in art:
                    print('Ваше слово относится к искусству')
                elif word.lower() in nature:
                    print('Ваше слово относится к природе')
                hint_used_category = True
                print("Вы использовали подсказку!")

        word_input = input('Введите букву: ').upper()

        if not is_valid(word_input):
            print('Введите одну букву!')
            continue

        if word_input in guessed_letters:
            print('Вы уже называли эту букву!')
            continue

        guessed_letters.append(word_input)

        if word_input in word:
            print('Отличная работа! Эта буква есть в слове.')
            for i in range(len(word)):
                if word[i] == word_input:
                    word_as_list[i] = word_input
            word_completion = ''.join(word_as_list)

            if '_' not in word_completion:
                guessed = True
        else:
            print('Этой буквы нет в слове!')
            tries -= 1

        print(display_hangman(tries))
        print(word_completion)
        print(f'Осталось попыток: {tries}')
        print(f'Названные буквы: {", ".join(guessed_letters)}')

    if guessed:
        print('Поздравляем, вы угадали слово! Вы победили!')
    else:
        print(f'Вы проиграли! Загаданное слово было: {word}')


while True:
    play(get_word())
    repeat = input('Хотите сыграть ещё? (да/нет): ').lower()

    if repeat != 'да':
        print('Спасибо, что играли в угадайку слов. Еще увидимся...')
        break
