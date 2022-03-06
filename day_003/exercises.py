print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age >= 45 and age <= 55:
        print("Everything is going to be ok.  Have a free ride on us!")
    elif age >= 18:
        bill = 12
        print("Adult tickets are $12.")
    elif age >= 12:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 5
        print("Child tickets are $5.")
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")

# Exercise #1
print("\nExercise #1")
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")


# Exercise #2
print("\nExercise #2")
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆
#W rite your code below this line 👇
bmi = weight / (height ** 2)
if bmi >= 35:
    print(f"Your BMI is {round(bmi)}, you are clinically obese.")
elif bmi >= 30:
    print(f"Your BMI is {round(bmi)}, you are obese.")
elif bmi >= 25:
    print(f"Your BMI is {round(bmi)}, you are slightly overweight.")
elif bmi >= 18.5:
    print(f"Your BMI is {round(bmi)}, you have a normal weight.")
else:
    print(f"Your BMI is {round(bmi)}, you are underweight.")


# Exercise #3
print("\nExercise #3")
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
if year % 4 == 0:
    if year % 100 != 0:
        print("Leap Year")
    elif year % 400 == 0:
        print("Leap Year")
    else:
        print("Not leap year.")
else:
    print("Not leap year.")


    # Exercise #4
    print("\nExercise #4")
    # 🚨 Don't change the code below 👇
    print("Welcome to Python Pizza Deliveries!")
    size = input("What size pizza do you want? S, M, or L ")
    add_pepperoni = input("Do you want pepperoni? Y or N ")
    extra_cheese = input("Do you want extra cheese? Y or N ")
    # 🚨 Don't change the code above 👆
    # Write your code below this line 👇
    bill = 0
    if size == "S":
        bill = 15
        if add_pepperoni == "Y":
            bill += 2
    elif size == "M":
        bill = 20
        if add_pepperoni == "Y":
            bill += 3
    else:
        bill = 25
        if add_pepperoni == "Y":
            bill += 3
    if extra_cheese == "Y":
        bill += 1

    print(f"Your final bill is: ${bill}")


    # Exercise #5
    print("\nExercise #5")
    # 🚨 Don't change the code below 👇
    print("Welcome to the Love Calculator!")
    name1 = input("What is your name? \n")
    name2 = input("What is their name? \n")
    # 🚨 Don't change the code above 👆
    # Write your code below this line 👇
    lower_name1 = name1.lower()
    lower_name2 = name2.lower()
    combined_lower_names = lower_name1 + lower_name2
    first_digit = combined_lower_names.count("t")
    first_digit += combined_lower_names.count("r")
    first_digit += combined_lower_names.count("u")
    first_digit += combined_lower_names.count("e")
    second_digit = combined_lower_names.count("l")
    second_digit += combined_lower_names.count("o")
    second_digit += combined_lower_names.count("v")
    second_digit += combined_lower_names.count("e")
    result = first_digit * 10 + second_digit

    if result < 10 or result > 90:
        print(f"Your score is {result}, you go together like coke and mentos.")
    elif result >= 40 and result <= 50:
        print(f"Your score is {result}, you are alright together.")
    else:
        print(f"Your score is {result}")