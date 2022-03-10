programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Retrieving items from dictionary.
print(programming_dictionary["Bug"])

# Adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."

# Create an empty dictionary.
empty_dictionary = {}

# Wipe an existing dictionary.
# programming_dictionary = {}

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."

# Loop through a dicitonary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# Exercise #1
print("\nExercise #1")
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
# TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    if student_scores[key] > 90:
        student_grades[key] = "Outstanding"
    elif student_scores[key] > 80:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] > 70:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"
# 🚨 Don't change the code below 👇
print(student_grades)


# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a List in a Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting Dictionary in a Dictionary
enhanced_travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 4,
    },
    "Jamaica": {
        "cities_visited": ["Montego Bay"],
        "total_visits": 1,
    },
}

# Nesting Dictionary in a List
another_travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 4,
    },
    {
        "country": "Jamaica",
        "cities_visited": ["Montego Bay"],
        "total_visits": 1,
    },
]

# Exercise 2
print("\nExercise #2")
new_travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above
#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇


def add_new_country(country, visits, cities):
    new_travel_log.append({
        "country": country,
        "visits": visits,
        "cities": cities,
    })


#🚨 Do not change the code below
add_new_country("Italy", 2, ["Rome", "Milan", "Florence"])
print(new_travel_log)
