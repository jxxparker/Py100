import random #importing random fxn
from hangman_words import word_list 

chosen_word = random.choice(word_list) #chooses a random word from word_list
word_length = len(chosen_word) 

end_of_game = False
lives = 6

from hangman_art import logo, stages
print(logo)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"you've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:

        print(f"you guessed {guess}, thats not in the word. you lose a")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
    print(stages[lives])