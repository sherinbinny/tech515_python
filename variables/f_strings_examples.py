# ----------------------------
# F-STRINGS
# ----------------------------

# Starting code:

name = "Lassie"
years = 7
height_cm = 60.2
# print these variables in an f-string so that it outputs this to the screen:
# "Lassie is 7 years old and 60.2 cm tall."

print(f"{name} is {years} years old and {height_cm} cm tall.")



# Use f-strings to format numbers
# Starting code:

pi = 3.14159265359

# Use an f-string to print pi to 3 decimal places e.g. 'Pi to 3 decimal places: <value>'
print(f"Pi to 3 dp: {pi:.3f}")

# Use an f-string to print pi to 5 decimal places e.g. 'Pi to 5 decimal places: <value>'
print(f"Pi to 5 dp: {pi:.5f}")

score = 16
max_score = 26
score_as_decimal = score / max_score

# Use an f-string to print 'score_as_decimal' e.g. 'You scored 0.6153846153846154' (no % sign)
print(f"You scored {score_as_decimal}")

# Use an f-string to print 'score_as_decimal' formatted as a percentage e.g. 'You scored 61.538462%'
print(f"You scored {score_as_decimal:%}")

# Use an f-string to print 'score_as_decimal' formatted as a percentage to rounded to 2 decimal places e.g. 'You scored 61.54%'
print(f"You scored {score_as_decimal:.2%}")

# Use an f-string to print 'score_as_decimal' formatted as a percentage to rounded to a whole number e.g. 'You scored 62%'
print(f"You scored {score_as_decimal:.0%}")





# Consolidation Task: Improve on previous task to capture user details
# Improve on the task where you captured the name, DOB and age of the user and printed them to the screen
# Now ask for user for the details show below and produce the output as shown.

name = input("What is your name? ")
month = input("What month were you born? ")
year = input("What year were you born? ")

# In the process, you should:
# Convert the age inputted to an integer
age = int(input("What is your age? "))

# Use concatenation so that you are forced to convert the age back to a string (or use an alternative method than concatenation or f-strings so that you don't need to convert back to a string)
print("Hi " + name + ", " + str(age))

# Use an f-string at least once
print(f"You were born in {month} of the year {year}.")

# The screen output should be:
# What is your name? Ramon
# What is your age? 23
# What month were you born? October
# What year were you born? 2002
# Hi Ramon, 23
# You were born in October of the year 2002.
