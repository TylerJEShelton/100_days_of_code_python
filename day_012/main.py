from art import logo
import random

MAX_NUMBER = 100


# Function to check the answer
def check_guess(current_guess, answer):
    if current_guess < 1 or current_guess > MAX_NUMBER:
        print(f"You guessed a number outside the range of 1 to {MAX_NUMBER}.  You wasted a guess.  Guess again.")
    elif current_guess < answer:
        print("Your guess was too low.")
    elif current_guess > answer:
        print("Your guess was too high.")
    else:
        print(f"Congrats! You guessed it! The answer was {answer}.")
        return True
    return False


# Function to set the number of guesses
def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == "easy":
        # Easy difficulty
        return 10
    elif difficulty == "hard":
        # Hard difficulty
        return 5
    else:
        print("You selected an invalid choice so I guess you like things difficult.")
        # Insane difficulty
        return 3


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and {MAX_NUMBER}.")
    correct_answer = random.randint(1, MAX_NUMBER + 1)
    is_guessing = True

    # For testing purposes only
    # print(f"The answer is {correct_answer}")

    num_guesses = set_difficulty()

    while is_guessing:
        print(f"You have {num_guesses} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if not check_guess(guess, correct_answer):
            num_guesses -= 1
            if num_guesses == 0:
                # If the player runs out of guesses, end the game
                print("Sorry, you have no more guesses left. You lose. Better luck next time.")
                is_guessing = False
            else:
                print("Guess again!")
        else:
            # If the guess was correct, end the game
            is_guessing = False

    if input("Would you like to play again? Type 'yes' or 'no': ") == "yes":
        game()

# Start the game loop
game()
