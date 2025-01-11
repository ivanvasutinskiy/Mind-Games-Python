from random import randint

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def start_game():
    ANSWER = randint(1, 100)

    if ANSWER % 2 == 0:
        is_even = 'yes'
    else:
        is_even = 'no'

    return (ANSWERr, is_even)