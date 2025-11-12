# ----------------------------
# YEAR OF BIRTH CALCULATOR
# ----------------------------

# Summary
# Write a Python script to calculate the user's year of birth

# The task

# First part
# define the variables age_int and name_str (set dummy/default/initial values)
# make a calculation for the year in which the person was born
# print out "OMG , you are years old so you were born in " with the correct values


from datetime import datetime  # Import the datetime module to get the current year
current_year = datetime.now().year # Gets the current year from the computer’s clock

age_int = 31
name_str = "Sherin"
birth_year = current_year - age_int
print(f"OMG {name_str}, you are {age_int} years old so you were born in {birth_year}!")

# Second Part
# prompt the user for inputs and assign the variable age_int and name_str
# remove the initial values set

name_str = input("What is your name? ")
age_int = int(input("What is your age? "))
birth_year = current_year - age_int
print(f"OMG {name_str}, you are {age_int} years old so you were born in {birth_year}!")

# Third Part
# calculate and print out the total number of hours this person has lived

hours_lived = age_int * 365 * 24
print(f"You have lived approximately {hours_lived:,} hours so far!")


# If time
# figure out a way to account for if the persons birthday has already happened this year or not

from datetime import date

today = date.today()
current_year = today.year

name = input("What is your name? ")
age = int(input("What is your age? "))
birth_month = int(input("Enter your birth month as a number (1-12): "))
birth_day = int(input("Enter your birth day: "))

birth_year = current_year - age
birthday_this_year = date(current_year, birth_month, birth_day)

if today < birthday_this_year:
    # If not yet had birthday, subtract one more year
    birth_year -= 1
    print("(Your birthday hasn’t happened yet this year.)")
else:
    print("(You’ve already celebrated your birthday this year!)")


# go look into the library 'time' to be more accurate with the hours lived
# show in your script that you have evaluated the methods of calculating the hours lived to see which is more accurate

import time
birthdate = datetime(birth_year, birth_month, birth_day)
birth_date_to_seconds = time.mktime(birthdate.timetuple())
current_date_to_seconds = time.time()
seconds_lived = current_date_to_seconds - birth_date_to_seconds
hours_accurate = seconds_lived/3600

print(f"You have lived approximately {hours_accurate:,.0f} hours.")


# Method 1 is the simplest but least accurate because it assumes every year has 365 days
# Method 2 (time) is the most accurate, as it measures every second lived since birth


# Acceptance Criteria
# program defines the variable age_int and name_str
# program prints the string "OMG <person>, you are <age> years old so you were born in <year>"



