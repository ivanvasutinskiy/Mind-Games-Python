from random import randint
from brain_games.cli import welcome_user




def main():
    name = welcome_user()

    flag = True
    print('Answer "yes" if the number is even, otherwise answer "no".')
    n = 0
    while n!=3: 
        num = randint(1, 100)
        if num % 2 == 0:
            flag = True
        else:
            flag = False

        print(f'Question: {num}')
        answer = input('Your answer: ')
        if answer == 'yes' and flag == True:
            print('Correct!')
            n +=1
        elif answer == 'no' and flag == False:
            print('Correct!')
            n +=1
        else:
            if answer == 'yes':
                print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!")
                break
            elif answer == 'no':
                print(f"'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}!")
                break
            else:
                print(f"use only 'yes' or 'no'.\nLet's try again, {name}!")
                break
            

    if n == 3:
        print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()




