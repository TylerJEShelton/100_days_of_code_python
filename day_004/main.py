rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

choices = [rock, paper, scissors]
text_choices = ["Rock", "Paper", "Scissors"]
computer_choice = random.randint(0, 2)
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice > 2 or user_choice < 0:
    print("You selected an invalid number. Try again later.")
else:
    print(f"You chose {text_choices[user_choice]}.")
    print(choices[user_choice])
    print(f"Computer chose {text_choices[computer_choice]}.")
    print(choices[computer_choice])

    if user_choice == computer_choice:
        print(f"Draw, you both chose {text_choices[user_choice]}")
    elif user_choice == 0:
        if computer_choice == 1:
            print("You Lose, Paper covers Rock.")
        else:
            print("You Win, Rock crushes Scissors.")
    elif user_choice == 1:
        if computer_choice == 0:
            print("You Win, Paper covers Rock.")
        else:
            print("You Lose, Scissors cuts Paper.")
    else:
        if computer_choice == 0:
            print("You Lose, Rock crushes Scissors.")
        else:
            print("You Win, Scissors cuts Paper.")