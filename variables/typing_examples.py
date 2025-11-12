# ----------------------------
# STRONGLY & DYNAMICALLY TYPED
# ----------------------------

# What does it mean that Python is
# A strongly typed language? Compare to a weakly typed language. Include a code example
# Python is strongly typed because it doesn’t automatically convert between incompatible types.

# This will cause an error
# print("5" + 5)

# Correct way: convert one type
print(int("5") + 5)   # 10

# In a weakly typed language like JavaScript, the conversion happens automatically:
# console.log("5" + 5); // outputs "55" (string)



# A dynamically typed language? Compare to a statically typed language. Include a code example
# Python decides the type of variable when the program runs, not before.
x = 10
print(type(x))  # <class 'int'>
x = "Now I’m a string"
print(type(x))  # <class 'str'>

# Statically typed languages (like Java or C#) need type declarations upfront
# int x = 10;
# x = "Now I’m a string"; // Error, type can’t change



# Overwrite the value of one of your variables which stores a number
# Check the id() of the variable before and after you overwrite the variable with a new number
num = 10
print("Before:", id(num))
num = 20
print("After:", id(num))


# Why does the 'id' of the variable change?
# Checking variable id before and after reassignment
# Every object in Python has a unique id(), which is its memory address.
# When you reassign a value, Python creates a new object in memory, so the ID changes.



# Assign one variable to another
# Start with this code:
# x = 10
# y = x
# Check the id of x and y
x = 10
y = x
print(id(x), id(y))  # same memory ID, same object

# Explain why the id of x and y are the same
# when we assign y = x, both variables point to the same object in memory, so they share the same id

# What happens if after assigning x = y, I give x a different value? Does the id of y change also?
x = 15
print(id(x), id(y))  # different ids after x changes
# y keeps its old value because integers are immutable, meaning that once an object is created, its value cannot be changed.
# Any modification creates a completely new object in memory instead of altering the original one.



# ----------------------------
# USER INPUT
# ----------------------------
# name = input("Enter your name: ")
# print("Hi", name)

# Getting multiple inputs
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# dob = input("Enter your date of birth (e.g. 12/09/1994): ")
# print(f"Hi {name}, you are {age} years old. Your DOB is {dob}.")
