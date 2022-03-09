# Step 5

import random
from hangman_words import word_list
from hangman_art import stages, logo

chosen_word = random.choice(word_list)
game_over = False
lives = 6
guess_list = []

# create blanks
display = []
for _ in chosen_word:
    display.append("_")

print(logo)

# FOR TESTING PURPOSES ONLY
# print(f"The solution is {chosen_word}")

while not game_over:
    print(stages[lives])
    # Join all the elements in the list and turn it into a String.
    print(f"\n{' '.join(display)}")
    guess = input("\nGuess a letter you think is in the word: ").lower()

    if guess in guess_list:
        print(f"\nYou already guessed {guess}, try again.")
    else:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = guess
        guess_list.append(guess)
        if guess not in chosen_word:
            print(f"\nSorry, {guess} is not in the word.  Try again.")
            lives -= 1


        # Check if user has got all letters or the user has no lives left.
        if "_" not in display or lives == 0:
            game_over = True

print(stages[lives])
if lives == 0:
    print(f"\nYou lose!  The word was {chosen_word}.  Better luck next time!")
else:
    print(f"\nCongratulations!  You have guessed the word {chosen_word} correctly!  You win!")