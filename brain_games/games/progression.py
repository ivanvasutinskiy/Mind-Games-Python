from random import choice, randint

RULES = 'What number is missing in the progression?'


def start_game():
    step = randint(1, 11)
    rang = randint(12, 16)

    progression = []

    for i in range(2, rang):
        num = step * i
        progression.append(str(num))

    answer = choice(progression)
    question = ' '.join(progression)
    question = question.replace(answer, '..', 1)
    return (question, answer)
