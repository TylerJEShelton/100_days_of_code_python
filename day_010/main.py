from art import logo

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
def calculator():
    print(logo)
    calculating = True
    num1 = float(input("What's the first number?: "))
    operation_string = ""
    for operand in operations:
        operation_string += operand + "  "
    print(operation_string)

    while calculating:
        selected_operation = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        result = operations[selected_operation](num1, num2)

        print(f"{num1} {selected_operation} {num2} = {result}")

        continue_calculating = input(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation, or type exit to quit: ").lower()
        if continue_calculating == "exit":
            calculating = False
        elif continue_calculating != "y":
            calculating = False
            calculator()
        else:
            num1 = result

calculator()