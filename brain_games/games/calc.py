from operator import add, mul, sub
from random import choice, randint

RULES = 'What is the result of the expression?'

OPERATIONS = [("+", add), ("-", sub), ("*", mul)]


def start_game():
    NUM1, NUM2 = randint(1, 100), randint(1, 100)

    operator, func = choice(OPERATIONS)
    question = f'{NUM1} {operator} {NUM2}'
    correct = func(NUM1, NUM2)

    return (question, str(correct))




    

