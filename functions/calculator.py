# ----------------------------
# Calculator
# ----------------------------


# Create a Python file called calculator.py and complete a viable basic calculator using functions....
# MVP (each of these should be in a separate function):
# Can add 2 numbers
# Can subtract 2 numbers
# Can multiply 2 numbers
# Can divide 2 numbers

# Taking it to the next level:
# Implement more complex operations, such as handling parentheses, exponentiation
# More advanced operations should continue to be broken into separate functions


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


print(add(10, 5))
print(subtract(10, 5))
print(multiply(10, 5))
print(divide(10, 5))
print(divide(10, 0))  # Error handling


def power(a, b):
    return a ** b


import math


def square_root(n):
    if n < 0:
        return "Error: Negative number"
    return math.sqrt(n)


def calculate_expression(expression):
    try:
        return eval(expression)
    except:
        return "Invalid expression"


print(power(2, 5))
print(square_root(25))
print(calculate_expression("(2 + 3) * 4"))
print(calculate_expression("10/(2+3)"))
