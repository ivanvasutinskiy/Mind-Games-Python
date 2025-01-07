from operator import add, mul, sub
from random import choice, randint

RULES = 'What is the result of the expression?'

OPERATIONS = [("+", add), ("-", sub), ("*", mul)]


def start_game():
    num1, num2 = randint(1, 100), randint(1, 100)

    operator, func = choice(OPERATIONS)
    question = f'{num1} {operator} {num2}'
    correct = func(num1, num2)

    return (question, str(correct))




    

