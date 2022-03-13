from game_data import data
from art import logo, vs
from random import randint
import os


def clear_console():
    '''This function clears the console'''

    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def choice_data(choice):
    '''This function takes a choice data dictionary and returns a formatted string'''

    choice_name = choice["name"]
    choice_desc = choice["description"]
    choice_country = choice["country"]
    return f"{choice_name}, a {choice_desc}, from {choice_country}."


def check_for_highest(follow_a, follow_b):
    '''This function checks to see which choice inputs has the most followers and returns 'A' or 'B' '''

    if follow_a > follow_b:
        return "A"
    else:
        return "B"


def check_choice(user_choice, answer):
    '''This function compares the user's choice with the answer and returns True or False'''

    if user_choice == answer:
        return True
    else:
        return False


score = 0
has_lost = False
possible_choices = len(data)

print(logo)

choice_a = randint(0, possible_choices - 1)

while not has_lost:
    choice_b = randint(0, possible_choices - 1)
    while choice_a == choice_b:
        choice_b = randint(0, possible_choices - 1)

    choice_a_followers = data[choice_a]["follower_count"]
    choice_b_followers = data[choice_b]["follower_count"]

    print(f"Compare A: {choice_data(data[choice_a])}")
    print(vs)
    print(f"Against B: {choice_data(data[choice_b])}")
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    clear_console()
    print(logo)

    if check_choice(guess, check_for_highest(choice_a_followers, choice_b_followers)):
        score += 1
        print(f"That's correct! Your current score is: {score}")
        choice_a = choice_b
    else:
        print(f"Sorry, that's incorrect. Your final score is: {score}")
        has_lost = True
