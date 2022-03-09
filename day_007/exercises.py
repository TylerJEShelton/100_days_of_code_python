# Step 1
import random

word_list = ["ardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word

chosen_word = random.choice(word_list)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess.  Make guess lowercase.

guess = input("Guess a letter you think is in the word: ").lower()
print(guess)

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for letter in chosen_word:
    if letter == guess:
        print("Correct")
    else:
        print("Incorrect")


# Step 2
import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(f"The solution is {chosen_word}")

# TODO-1 - Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# If the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter.
display = []
for _ in chosen_word:
    display.append("_")
print(display)

guess = input("\nGuess a letter you think is in the word: ").lower()

# TODO-2 - Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen_word was "apple", then display should be ["_", "p", "p", "_", "_"]

for index, letter in enumerate(chosen_word):
    if letter == guess:
        display[index] = guess

# TODO-3 - Print 'display' and you should see the guessed letter in the correct position and every other letter as "_"

print(display)

# Step 3
import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(f"The solution is {chosen_word}")

# create blanks
display = []
for _ in chosen_word:
    display.append("_")
print(display)

# TODO-1 - Use a while loop to let the user guess again.
# The loop should only stop once the user has guessed all the letters and 'display' has no more blanks.
# Then tell the user they have won.

game_over = False
while not game_over:
    guess = input("\nGuess a letter you think is in the word: ").lower()

    for index, letter in enumerate(chosen_word):
        if letter == guess:
            display[index] = guess

    print(display)
    if "_" not in display:
        game_over = True

print(f"\nCongratulations!  You have guessed the word {chosen_word}!  You win!")

# Step 4

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

game_over = False
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.
lives = 6

# create blanks
display = []
for _ in chosen_word:
    display.append("_")

# FOR TESTING PURPOSES ONLY
print(f"The solution is {chosen_word}")

while not game_over:
    print(stages[lives])
    # Join all the elements in the list and turn it into a String.
    print(f"\n{' '.join(display)}")
    guess = input("\nGuess a letter you think is in the word: ").lower()

    for index, letter in enumerate(chosen_word):
        if letter == guess:
            display[index] = guess

    # TODO-2: - If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop and it should print "You lose."

    if guess not in chosen_word:
        lives -= 1

    # Check if user has got all letters or the user has no lives left.
    if "_" not in display or lives == 0:
        game_over = True
    # TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.


print(stages[lives])
if lives == 0:
    print(f"\nYou lose!  The word was {chosen_word}.  Better luck next time!")
else:
    print(f"\nCongratulations!  You have guessed the word {chosen_word} correctly!  You win!")

