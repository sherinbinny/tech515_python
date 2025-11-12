# ----------------------------
# STRING SLICING
# ----------------------------


# What is slicing strings?
# Slicing means extracting parts (substrings) from a string using index positions.

# Here is your starting code. You may need to:
# Write code to do what the comments ask for.
# Write a comment to explain what the code does.

Hw = "Hello world!"

print(Hw)

# Find out how many characters Hw has
print(len(Hw))      # total characters

# Get the character in the first position in Hw
print(Hw[0])        # first character

# Get the last character
print(Hw[-1])       # last character

# Get the 2nd last character
print(Hw[-2])

# Write a comment to EXPLAIN what does this do
print(Hw[2:])
# from index 2 to end → 'llo world!'

# Write a comment to EXPLAIN what does this do
print(Hw[-3:])
# last 3 characters → 'ld!'

# Write a comment to EXPLAIN what does this do
print(Hw[:5])
# from start to before index 5 → 'Hello'

# Starts from the second, stops at the fifth (doesn't include it)
print(Hw[1:5])






# ----------------------------
# Consolidation Task: Finish the guessing game with string slicing
# ----------------------------

# Starting code:

# Guess the word with 4 hints to help
# Rationale: Practice word slicing
# Type of exercise: Finish the code

original_word = "recommendation"
scrambled_word = "eoommandretnic"

# Create the hint slices...

# TO DO: On the next line, replace "?" with a string slice in the format "original_word[x:y]". Use the hints below to know what slice is needed

hint1_slice = original_word[4:6]

# TO DO: On the next line, replace "?" with a string slice in the format "original_word[x:y]". Use the hints below to know what slice is needed

hint2_slice = original_word[-3:]

# TO DO: On the next line, replace "?" with a string slice in the format "original_word[x:y]". Use the hints below to know what slice is needed

hint3_slice = original_word[7:10]

# TO DO: On the next line, replace "?" with a string slice in the format "original_word[x:y]". Use the hints below to know what slice is needed

hint4_slice = original_word[:2]

# Game instructions

print("Scrambled word:", scrambled_word)

print("Guess the original word from the scrambled version.")

print("Here are some hints:")

# Hints based on list slicing

print("Hint 1: The 5th and 6th letters are '" + hint1_slice + "'.")

print("Hint 2: The last 3 letters are '" + hint2_slice + "'.")

print("Hint 3: The 8th to 10th letters are '" + hint3_slice + "'.")

print("Hint 4: The first two letters are '" + hint4_slice + "'.")

# Game ends here

print("What's your guess?")