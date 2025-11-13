# ----------------------------
# List slicing
# ----------------------------

# You have probably already covered string slicing
# List slicing is similar, except we are cutting up a list of item rather than a string of characters
# Starting code:

mixture = [1, 2, 3, "one", "two", "three"]
print(mixture)


# Print these list slices to the screen:
# Returns the 2nd and 3rd items in the list -> It should return [2, 3]
# Returns every second item in the list -> It should return [1, 3, 'two']
# Start at the last item, stop at the 3rd last item, and step in reverse order -> It should return ['three', 'two']


# 2nd and 3rd items
print("2nd and 3rd items:", mixture[1:3])

# Every second item
print("Every second item:", mixture[::2])

# Start at the last, stop at the 3rd last, step backwards
print("Reverse slice:", mixture[-1:-4:-1])

