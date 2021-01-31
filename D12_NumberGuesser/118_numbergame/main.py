from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
#fxn to check user's guess against actual answer
def check_answer(guess, answer):
    if guess > answer:
        print("too high")
    elif guess < answer:
        print("too low")
    else:
        print(f"you got it. the answer was {answer}")
        
#make fxn to set difficulty
def set_difficulty():
    level = input("choose a difficulty. type 'easy' or 'hard: ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

        


def game():
#choose a random number btw 1 -100
    print("welcome to number guessing game")
    print("i'm thinking of a number btw 1 and 100")
    answer = randint(1, 100)
    print(f"psst the correct anser is {answer}")

    turns = set_difficulty()
    print(f"you have {turns} attempts remaining to guess the number ")


    #repeat the guessing fxn if they get it wrong]
    guess = 0
    while guess != answer:
    #let the user guess a number
        guess = int(input("Make a guess: "))
        check_answer(guess, answer)

#track the number of turns and reduce by 1 if they get it wrong.
game()