# Exercise #1
print("Exercise #1:")
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆
####################################
#Write your code below this line 👇
num1 = int(two_digit_number[0])
num2 = int(two_digit_number[1])

result = num1 + num2
print(result)

# Exercise #2
print("Exercise #2:")
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = float(weight) / (float(height) ** 2)
print(int(bmi))

# Exercise #3
print("Exercise #3:")
# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇

years_left = 90 - int(age)
months = years_left * 12
weeks = years_left * 52
days = years_left * 365

print(f"You have {days} days, {weeks} weeks, and {months} months left.")