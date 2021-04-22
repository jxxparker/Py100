word_list = ["aardvark", "baboon", "camel"]
import random

chosen_word = random.choice(word_list) #chosen_word becomes one of random word from above
print(chosen_word) #printing random word

guess = input("Guess a letter: ").lower() #guess becomes the letter user guesses after becoming lower case

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")