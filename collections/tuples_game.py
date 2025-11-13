# ----------------------------
# Tuples
# ----------------------------

# How are tuples similar to lists?
# Tuples and lists are similar because they both store multiple items in an ordered sequence.
# This means the items keep the same position, they can be accessed using their index number, and they can hold a mixture of data types together within one structure.
# Both are used when you want to group related information in one place.


# Are tuples immutable and what does this mean?
# Yes, tuples are immutable.
# This means that once a tuple is created, none of its contents can be changed.
# You cannot add new items, remove items, or modify existing values inside it.
# If you need a different version of the data, you must create a completely new tuple instead of altering the old one.
# Immutability means the data stays exactly as it was originally created.
# This is the opposite of a list, which can be modified.


# What other data types are immutable?
# Common immutable data types in Python include strings, integers, floats, booleans, and frozen sets.
# For all of these types, any attempt to "change" their value actually results in Python creating a new object in memory rather than modifying the original one.


# What are good use cases for tuples instead of lists?
# Tuples are ideal when you want to store data that must remain fixed and shouldn’t be accidentally changed while a program runs.
# They are useful for representing constant sets of values (such as days of the week), structured pieces of data that naturally belong together (such as coordinates or dimensions), or when you want to ensure the integrity of information by preventing accidental modification.
# Tuples are also useful in places where Python requires immutable data, such as when using them as dictionary keys or storing them inside sets.


# What does the following piece of code do?

essentials = ("bread", "eggs", "milk") #Creates an immutable tuple with three items:
print(essentials) #Outputs the entire tuple exactly as it is.
print(essentials.count("bread")) #returns how many times "bread" appears in the tuple.



# The task
# Add your code where it says 'YOUR CODE GOES HERE'
# Starting code:

# "Stranded on a Desert Island" game
# Rationale: Practice tuples
# Type of exercise: Finish the code
print("You are stranded on a desert island. You can take only THREE items.")
essential_item1 = input("What is an essential item you would take? ")
essential_item2 = input("What is an essential item you would take? ")
essential_item3 = input("What is an essential item you would take? ")
# save the items as a tuple
essentials_tuple = (essential_item1, essential_item2, essential_item3)  # YOUR CODE GOES HERE INSTEAD OF 'None'
# print the tuple
print("Here are your items as a tuple:", essentials_tuple)
print("")
print("I lied. You can take one more item.")
essential_item4 = input("What is one more essential item you would take? ")
# try to add the 4th item to the tuple
# if you can't add the 4th item, work out how to save the 4th item to the tuple
# YOUR CODE GOES HERE

essentials_tuple = essentials_tuple + (essential_item4,)

print("Here are your items as a tuple (with the 4th item added):", essentials_tuple)