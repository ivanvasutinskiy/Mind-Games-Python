from random import randint

RULES = 'Answer "yes" if number even otherwise answer "no".'


def start_game():
    answer = randint(1, 100)

    if answer % 2 == 0:
        is_even = 'yes'
    else:
        is_even = 'no'

    return (answer, is_even)