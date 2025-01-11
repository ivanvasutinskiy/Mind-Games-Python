from random import randint

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'

ANSWER = randint(1, 100)


def start_game():
    if ANSWER % 2 == 0:
        is_even = 'yes'
    else:
        is_even = 'no'

    return (ANSWER, is_even)