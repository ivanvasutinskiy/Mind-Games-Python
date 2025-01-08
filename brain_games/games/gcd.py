from random import randint

RULES = 'Find the greatest common divisor of given numbers.'


def start_game():
    n1, n2 = randint(1, 100), randint(1, 100)

    max_divisor = min(n1, n2)
    
    for num in range(1, max_divisor + 1):
        if n1 % num == 0 and n2 % num == 0:
            answer = num

    question = f'{n1} {n2}'  

    return (question, str(answer))