# ----------------------------
# CONCATENATION & CASTING
# ----------------------------

# What is concatenation? Give a simple example with your code.
# Concatenation simply means joining two or more strings together to form one longer string.


# Your starting code:

x = 2

y = 5.4

z = " there's now a number 25.4 unless we put a space in!"



# print(x + y + z) # This will fail:

# Make it work:
# Make the print statement work using concatenation (+) to join x, y and z so that it prints this to the screen: `25.4 there's now a number 25.4 unless we put a space in!"
print(str(x + y) + z)  # Fix: convert numbers to string first

# Explain: The problem and the solution
# Problem:
# Python can’t combine numbers and strings directly.
# Solution:
# Convert numbers using str() or use an f-string,
# short for formatted string literals, are a way to embed variables or expressions directly inside a string by prefixing it with the letter f or F and placing the variable names inside curly braces {}.



# Starting code:
int_string = "6"
# convert int_string to an integer
num_int = int(int_string)

# after converting, print its data type to the screen
print(num_int, type(num_int))

# convert int_string to float
num_float = float(int_string)

# after converting, print its data type to the screen
print(num_float, type(num_float))
