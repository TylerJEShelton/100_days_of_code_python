fruits = ["Apple", "Peach", "Cherry"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
print(fruits)


# Exercise #1
print("\nExercise #1")
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
total = 0
students = 0
for height in student_heights:
    total += height
    students += 1
average = round(total / students)
print(average)


# Exercise #2
print("\nExercise #2")
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")

# For Loop with Range
for number in range(1, 11, 3):
    print(number)

total_number = 0
for number in range(1, 101):
    total_number += number
print(total_number)

# Exercise #3
print("\nExercise #3")
# Write your code below this row 👇
total_even = 0
for number in range(2, 101, 2):
    total_even += number
print(total_even)


# Exercise #4
print("\nExercise #4")
# Write your code below this row 👇
for number in range(1,101):
    if (number % 5 == 0) and (number % 3 == 0):
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
