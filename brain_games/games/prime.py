from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def start_game():
    NUM = randint(1, 100)
    total = 0

    for i in range(1, NUM + 1):
        if NUM % i == 0:
            total += 1
        
    question = f'{NUM}' 
    if total == 2:
        answaer = 'yes'
    else:
        answaer = 'no'

    return (question, answaer)
