

# How are tuples similar to lists?
#
#
# Are tuples immutable and what does this mean?
#
#
# What other data types are immutable?
#
#
# What are good use cases for tuples instead of lists?
#
#
# What does the following piece of code do?


essentials = ("bread", "eggs", "milk")

print(essentials)
print(essentials.count("bread"))


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
essentials_tuple = None  # YOUR CODE GOES HERE INSTEAD OF 'None'
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