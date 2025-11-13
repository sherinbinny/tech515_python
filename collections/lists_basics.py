# ----------------------------
# Working with a List
# ----------------------------

# Create a list called 'shopping_list' with the following items:
# eggs
# bread
# bananas
# biscuits
# milk
# Print the list to the screen
# Print the data type of 'shopping_list'
# Print the first item in the list
# Print the last item in the list
# Change the second item in the list (i.e. 'bread') to 'rice' instead, then print the second item to the screen to prove it's been changed
# Use the list's method to add the item 'carrots' to the list (you should not re-assign the list using '='), then check the length of the list (which should now have 6 rather than 5)
# Add another list with two items ('toffee' and 'coffee') to the 'shopping_list' list. Use one of the list's methods to add the two items in one go.
# Print the 'shopping_list' to check 'toffee' and 'coffee' have been added correctly.
# Remove "bananas" from 'shopping_list'. Print 'shopping_list' to check it's been removed.
# Remove the last item ('coffee') from 'shopping_list' using the pop method. Check it worked by printing 'shopping_list'



# Create the list
shopping_list = ["eggs", "bread", "bananas", "biscuits", "milk"]

# Print the list
print("Shopping list:", shopping_list)

# Print the data type
print("Data type:", type(shopping_list))

# Print the first and last items
print("First item:", shopping_list[0])
print("Last item:", shopping_list[-1])

# Change 'bread' to 'rice'
shopping_list[1] = "rice"
print("Updated second item:", shopping_list[1])

# Add 'carrots' using append()
shopping_list.append("carrots")
print("List after adding carrots:", shopping_list)
print("Length of list:", len(shopping_list))

# Add another list of two items ('toffee', 'coffee')
shopping_list.extend(["toffee", "coffee"])
print("After adding more items:", shopping_list)

# Remove 'bananas'
shopping_list.remove("bananas")
print("After removing bananas:", shopping_list)

# Remove the last item using pop()
shopping_list.pop()
print("After popping last item:", shopping_list)
