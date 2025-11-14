# ------------------------------
# Magic number guessing game
# ------------------------------


# User story 1
# As a user, I want to be able to guess a number and know if I got it correct or not, so that I can know if I won or not.
# Define/assign number to a variable called magic_number
# Ask user for input
# Check if this input matches magic_number
# Let the user know if the response was correct or not
# Allow the user 5 guesses


# magic_number = 7
# guesses_allowed = 5
# guesses_left = guesses_allowed
#
# print("Guess the magic number between 1 and 10.")
# print(f"You have {guesses_allowed} guesses.\n")
#
# while guesses_left > 0:
#     guess = input("Enter your guess: ")
#     guess = int(guess)
#
#     if guess == magic_number:
#         print("Correct! You guessed the magic number!")
#         break
#     else:
#         print("Wrong guess.")
#
#     guesses_left -= 1
#
# if guesses_left == 0:
#     print("Game over! You've used all your guesses.")

# User story 2
# As a user, I want to be able to guess a number and know if I need to go higher or lower.
# User story 3
# As a user, I don't want my guesses wasted if I enter something accidentally as my guess which are not digits.
# User story 4
# As a user, after each guess, I would like to know how many guesses I have left.


# magic_number = 7
# guesses_allowed = 5
# guesses_left = guesses_allowed
#
# print("Guess the magic number between 1 and 10.")
# print(f"You have {guesses_allowed} guesses.\n")
#
# while guesses_left > 0:
#     guess = input("Enter your guess: ")
#     if not guess.isdigit():
#         print("Invalid input. Please enter digits only.\n")
#         # don't reduce guesses, invalid input shouldn't count
#         continue
#
#     guess = int(guess)
#
#     if guess == magic_number:
#         print("Correct! You guessed the magic number!")
#         break
#
#     elif guess < magic_number:
#         print("Go HIGHER.")
#     else:
#         print("Go LOWER.")
#
#     guesses_left -= 1
#
#     print(f"You have {guesses_left} guesses left.\n")
#
# if guesses_left == 0:
#     print("Game over! You've used all your guesses.")

# User story 5
# As a user, I would like the magic to be randomly generated each time I play so it is more fun.
# User story 6
# As a user, I would like to know the magic number at the end of the game if I still haven't guessed correctly, and I've used up all my tries.
# Hint: Use the Python library random to generate a random number rather than assigning one


import random

magic_number = random.randint(1, 20)
guesses_allowed = 5
guesses_left = guesses_allowed

print("Guess the magic number between 1 and 20.")
print(f"You have {guesses_allowed} guesses.\n")

while guesses_left > 0:
    guess = input("Enter your guess: ")

    if not guess.isdigit():
        print("Invalid input. Please enter digits only.\n")
        continue

    guess = int(guess)

    if guess == magic_number:
        print("Correct! You guessed the magic number!")
        break
    elif guess < magic_number:
        print("Go HIGHER.")
    else:
        print("Go LOWER.")

    guesses_left -= 1
    print(f"You have {guesses_left} guesses left.\n")

if guesses_left == 0:
    print("You've used all your guesses!")
    print(f"The magic number was: {magic_number}")
