# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12
# Round the result to 2 decimal places.

print("Welcome to the tip calculator.")

bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people will be splitting the bill? ")

amount_to_pay = round((float(bill) / int(people)) * ((100 + int(tip)) / 100), 2)
amount_to_pay = "{:.2f}".format(amount_to_pay)
print(f"Each person should pay: ${amount_to_pay}")

