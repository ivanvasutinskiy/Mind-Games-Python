from brain_games.cli import get_answer, welcome_user

round = 3


def game_start(game):
    player = welcome_user(game.RULES)

    total = 0

    while total < round:

        question, correct = game.start_game()

        answer = get_answer(question)

        if answer != correct:
            print(f"{answer} is wrong answer ;(." 
            f"Correct answer was {correct}."
            f"\nLet's try again, {player}!")
            return
        print('Correct')
        total += 1

    print(f'Congratulations, {player}!')





        

