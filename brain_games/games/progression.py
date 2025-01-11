from random import choice, randint

RULES = 'What number is missing in the progression?'


def start_game():
    STEP = randint(1, 11)
    RANG = randint(12, 16)

    progression = []

    for i in range(2, RANG):
        num = STEP * i
        progression.append(str(num))

    answer = choice(progression)
    question = ' '.join(progression)
    question = question.replace(answer, '..', 1)
    return (question, answer)
