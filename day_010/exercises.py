# Functions with Outputs

def format_name(f_name, l_name):
    """Take a first and last name and format it
    to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid names."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"Here is your formatted name: {formatted_f_name} {formatted_l_name}"


first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
formatted_string = format_name(first_name, last_name)
print(formatted_string)


# Exercise #1
print("\nExercise #1")


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month > 12 or month < 1:
        return "Invalid month."
    if is_leap(year):
        month_days[1] = 29
    return month_days[month - 1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
