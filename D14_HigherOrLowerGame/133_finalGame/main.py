from game_data import data
import random
import os
from art import logo, vs


def format_data(account):
    """takes the account data and returns the printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    account_followers = account["follower_count"]
    return (f"name: {account_name}, a {account_descr}, from {account_country}, {account_followers}")


def check_answer(guess, a_followers, b_followers):
    """use if statement to check if user is correct"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


score = 0
game_should_continue = True
account_b = random.choice(data)
#make the game repeatable

while game_should_continue:
    #generate a random account from the game data.
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Compare B: {format_data(account_b)}.")

    #ask user for a guess.
    guess = input("who has more followers? Type 'A' or 'B'").lower()
    #check if user is correct
    #get follower count of each account.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    os.system('clear')
    print(logo)

    #give user feedback on their guess.
    if is_correct:
        score += 1
        print(f"You're right Current score: {score}")
    else: 
        game_should_continue = False
        print(f"Sorry, that's wrong. Final Score: {score}")



#CLEAR THE SCREEN