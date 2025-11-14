# ----------------------------
# FizzBuzz
# ----------------------------


# Summary
# Print incremented numbers to the screen but substitute multiples of 3 with 'Fizz', multiples of 5 with 'Buzz', and multiples of both with 'FizzBuzz'

# The task
# Core:
# Make a new 'fizzbuzz.py' file
# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz" instead of the number
# For numbers which are multiples of both three and five print "FizzBuzz".


# for num in range(1, 101):
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)


# If time:
# Improve the script so the user can decide which numbers to substitute for "Fizz" and "Buzz"

# fizz_num = int(input("Enter a number for Fizz: "))
# buzz_num = int(input("Enter a number for Buzz: "))
#
# for num in range(1, 101):
#     if num % fizz_num == 0 and num % buzz_num == 0:
#         print("FizzBuzz")
#     elif num % fizz_num == 0:
#         print("Fizz")
#     elif num % buzz_num == 0:
#         print("Buzz")
#     else:
#         print(num)

# Refactor using functions
# Acceptance Criteria
# All core tasks done
# Works with no errors


def fizzbuzz_value(num, fizz_num=3, buzz_num=5):
    if num % fizz_num == 0 and num % buzz_num == 0:
        return "FizzBuzz"
    elif num % fizz_num == 0:
        return "Fizz"
    elif num % buzz_num == 0:
        return "Buzz"
    else:
        return num


def run_fizzbuzz():
    for num in range(1, 101):
        print(fizzbuzz_value(num))


run_fizzbuzz()
