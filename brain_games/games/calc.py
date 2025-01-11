from operator import add, mul, sub
from random import choice, randint

RULES = 'What is the result of the expression?'

OPERATIONS = [("+", add), ("-", sub), ("*", mul)]

NUM1, NUM2 = randint(1, 100), randint(1, 100)


def start_game():
    operator, func = choice(OPERATIONS)
    question = f'{NUM1} {operator} {NUM2}'
    correct = func(NUM1, NUM2)

    return (question, str(correct))




    

