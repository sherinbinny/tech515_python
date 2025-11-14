# Group task: Make functions

# 1. Make a function with no argument
# Name it 'print_something' and all it should do it print something to the screen
# Call the function to test it works

def print_something():
    print("This is something!")


print_something()


# 2. Make a function with one argument
# Aim: Improve the last function by having it receive an argument to replace the 'hard coded' string
# Make a new improved function which
# Accepts a string variable as an argument
# Prints the string variable received as an argument

def print_message(msg):
    print(msg)


print_message("Hello Sherin!")


# 3. Make a more interesting version of a function that accepts one argument
# Here is the code to call the function:
# greet("Susan")
# You need to write the function
# Make sure the print statement in your function uses concatenation (ie. +) rather than an f-string
# Output should be:
# Hello, my name is Susan.

def greet(name: str):
    print("Hello, my name is " + name + ".")


greet("Susan")


# 4. Make a function with 2 arguments that returns a value
# Troubleshoot this code so that the function returns the correct value of 4:

def addition(int1, int2):
    return int1 + int2


print(addition(2, 2))


# This time we do NOT want the function to do the print to the screen
# Document what you've learnt

# Why it fails:
# It does not return anything. Python returns None by default.


# 5. Make a function with default values
# Copy your working code from the last exercise (that adds 2 and 2 together) as starting code for this exercise
# Replace line of code to call the function with this:

# print(addition())

# Run your code - you should get an error
# Modify your function so that int1 and int2 both have the default value of 2

def addition(int1=2, int2=2):
    return int1 + int2


print(addition())

# Run your code and make sure the result is 4
# Now call your function with this line of code:

print(addition(4, 4))


# Explain why the answer is now 8
# Because default values are ignored when you supply new values.
# Default values only matter when nothing is passed in.


# 6. Make a function that accepts any number of arguments
# Design a function called 'print_every_number' which accepts a tuple of numbers as an argument
# The function should do 2 things:
# Print the type of the tuple that was passed in as an arguments
# Loop through the tuple and print each item in the tuple on a separate line
# After calling the function, the output should be:

# <class 'tuple'>
# 1
# 2
# 2
# 3
# 3
# 4
# 5
# 5

def print_every_number(*numbers):
    print(type(numbers))
    for n in numbers:
        print(n)


print_every_number(1, 2, 2, 3, 3, 4, 5, 5)


# Explain what character allows your function to accept multiple arguments
# The asterisk * packs all arguments into a tuple.


# 7. Make a function which gives a hint about an argument's data type
# Some people think stricter typing should be used with Python as best practice, let's find out why
# See what happens if you call your earlier greet function with this line of code:
# greet(24601)

# To HELP us avoid this type of error, define the type of argument accepted into our function so that we are given a warning BEFORE we even run out Python script:
# Define that data type accepted by your greet function ids a string
# Notice that PyCharm now gives the warning Expected type 'str', got 'int' instead BEFORE you even run your code

# def greet(name: str):


# 8. Make a function which gives a hint about a return value's data type
# Let's make a new function to bring it all together, also to provide type hints for all arguments, function return values and variables used...
# The function should be named division:
# It should divide 2 integers accepted as arguments
# It should return the result of the division
# The arguments should:
# have their types defined
# have the default values of 2 and 5 (therefore, by default 2 will be divided by 5 and have the result 0.4)
# NEW! Define the value returned as a float for the type hint
# NEW! Before calling the function, define variables a and b in Python as statically-defined integers with the values 4 and 6
# You should call the function with this line of code
# print(division(a, b))
# Also check the default values work if no values are passed into the function

def division(a: int = 2, b: int = 5) -> float:
    return a / b


# Statically define variables
a: int = 4
b: int = 6

# Call the function
print(division(a, b))

# Test default values
print(division())  # should print 0.4

# What are some good practices when it comes to functions?
# ✔ Use meaningful names
# calculate_total() is better than ct().

# ✔ Keep them small & focused
# One function = one job.
# Not one function = kitchen sink.

# ✔ Use return values instead of print inside functions
# This makes your functions reusable.

# ✔ Use type hints
# Reduces bugs before runtime.

# ✔ Avoid global variables
# Data should be passed in, not magically imported from the sky.

# ✔ Use default arguments wisely
# But don’t use mutable defaults (lists/dicts).

# ✔ Document your function’s purpose
# Docstring = team happiness + fewer Slack messages.

# ✔ Make them predictable
# Same inputs should produce the same output.

# ✔ Don’t duplicate code
# If you copy-paste… your future self will cry.
