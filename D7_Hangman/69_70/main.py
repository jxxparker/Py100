import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = [] #empty list so we can add stuff to it 
word_length = len(chosen_word)
for _ in range(word_length): # _ is just used to use in for loops if nothing is used 
    display += "_"
print(display)

guess = input("Guess a letter: ").lower()
#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
print(display)