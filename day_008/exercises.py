# Review
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
    print("Hello!")
    print("How are you doing today?")
    print("Isn't the weather beautiful?")


greet()

# Function that allows for input


def greet_with_name(name):
    print(f"Hello {name}!")
    print(f"How are you doing today, {name}?")


greet_with_name("Tyler")

# Function with more than 1 input (Positional Arguments)


def greet_with(name, location):
    print(f"Hello {name}!")
    print(f"What is the weather like in {location}?")


greet_with("Tyler", "Toronto")

# Function with more than 1 input (Keyword Arguments)


def greet_with_keyword(name, location):
    print(f"Hello {name}!")
    print(f"What is the weather like in {location}?")


greet_with(location="Los Angeles", name="Marsha")

# Exercise 1
print("\nExercise #1")
#Write your code below this line 👇
import math
def paint_calc(height, width, cover):
    num_of_cans = height * width / cover
    full_cans_needed = math.ceil(num_of_cans)
    print(f"You'll need {full_cans_needed} cans of paint.")
#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.
# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


# Exercise 2
print("\nExercise #2")
# Write your code below this line 👇
def prime_checker(number):
    prime = True
    for num in range(2, number - 1):
        if number % num == 0:
            prime = False
    if prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
# Write your code above this line 👆
# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
