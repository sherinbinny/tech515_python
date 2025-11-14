# ----------------------------
# Mixing different data types in a list
# ----------------------------

# Use your code from the "Task: Python variable basics" (last subtask) where you asked the user for their name, age and DOB.
# Mix the name, age and DOB into one list user_details_list
# Print the user's name, age and DOB from the list
# Check the age is saved as an integer in the list.
# If it's not, work out how to convert it to an integer and add the age integer to the list.
# Ask the user for their height in cm and save it to the variable height
# Save height as a float in the list, and print the height from the list.


name = input("Enter your name: ")
age = int(input("Enter your age: "))
dob = input("Enter your date of birth (e.g. 13/02/1994): ")

# Combine into a list
user_details_list = [name, age, dob]

print("User details list:", user_details_list)
print("Name:", user_details_list[0])
print("Age:", user_details_list[1])
print("DOB:", user_details_list[2])
print("Type of age:", type(user_details_list[1]))

# Ask for height
height = float(input("Enter your height in cm: "))
user_details_list.append(height)

print(f"Height saved as: {user_details_list[3]} cm (type: {type(user_details_list[3])})")
