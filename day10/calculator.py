"""calculator
"""
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
num_1 = int(input("What's the first number?: "))

for char in operations:
    print(char)

OPERATION_SYMBOL = input("Pick an operation from the line above: ")

num_2 = int(input("What's the second number?: "))

calculation_function = operations[OPERATION_SYMBOL]
calculation_function(num_1, num_2)
answer = calculation_function(num_1, num_2)

print(f"{num_1} {OPERATION_SYMBOL} {num_2} = {answer}")
