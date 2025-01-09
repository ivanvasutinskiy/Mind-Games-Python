from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def start_game():
    num = randint(1, 100)
    total = 0

    for i in range(1, num + 1):
        if num % i == 0:
            total += 1
        

    question = f'{num}' 
    if total == 2:
        answaer = 'yes'
    else:
        answaer = 'no'

    return (question, answaer)
