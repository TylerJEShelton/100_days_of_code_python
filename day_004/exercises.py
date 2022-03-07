# import random
# import my_module
#
# random_integer = random.randint(1, 10)
# print(random_integer)
#
# print(my_module.pi)
#
# random_float = random.random() * 5
# print(random_float)
#
# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}")

# Exercise #1
print("\nExercise #1")
# Remember to use the random module
# Hint: Remember to import the random module here at the top of the file. 🎲
import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
# 🚨 Don't change the code above 👆 It's only for testing your code.
# Write the rest of your code below this line 👇
random_value = random.randint(0, 1)
if random_value == 0:
    print("Tails")
else:
    print("Heads")


# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts"]
# states_of_america[1] = "Pencilvania"
# states_of_america.append("Tylerstown")
# states_of_america.extend(["Kourtville", "ABariland"])
# print(states_of_america)


# Exercise #2
print("\nExercise #2")
import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
random_name = random.randint(0, len(names) - 1)
print(f"{names[random_name]} is going to buy the meal today!")


# Exercise #3
print("\nExercise #3")
# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆
#Write your code below this row 👇
row = int(position[0])
column = int(position[1])
map[column - 1][row - 1] = "X"
#Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")