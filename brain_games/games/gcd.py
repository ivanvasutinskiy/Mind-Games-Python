from random import randint

RULES = 'Find the greatest common divisor of given numbers.'


def start_game():
    N1, N2 = randint(1, 100), randint(1, 100)

    max_divisor = min(N1, N2)
    
    for num in range(1, max_divisor + 1):
        if N1 % num == 0 and N2 % num == 0:
            answer = num

    question = f'{N1} {N2}'  

    return (question, str(answer))