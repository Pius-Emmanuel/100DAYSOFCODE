"""calculator
"""
from art import LOGO
def add(n_1, n_2):
    """Adds two numbers"""
    return n_1 + n_2

def subtract(n_1, n_2):
    """Subtracts two numbers"""
    return n_1 - n_2

def multiply(n_1, n_2):
    """Multiplies two numbers"""
    return n_1 * n_2

def divide(n_1, n_2):
    """Divides two numbers"""
    return n_1 / n_2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/":divide
    }
def calculator():
    """ runs calculations with the user input"""
    print(LOGO)

    num_1 = float(input("What's the first number?: "))

    for char in operations:
        print(char)
    should_continue = True
    #we chose the symbol to calculate with
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num_2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num_1, num_2)

        print(f"{num_1} {operation_symbol} {num_2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num_1 = answer
        else:
            should_continue = False
            calculator()
calculator()
