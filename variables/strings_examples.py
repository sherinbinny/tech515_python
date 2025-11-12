# ----------------------------
# STRINGS AND QUOTES
# ----------------------------

# Starting code:
# bad_string = 'I said 'Wow!''
# print(bad_string)
# Explain: Why does this fail?
# causes SyntaxError (conflicting quotes)
# Python gets confused because it thinks the string ends at the second '.


# Find 3 ways to make this string work
# Condition: The Wow! must be surrounded in quotes when it prints to the screen
# Opinion: What is best practice when deciding what quotes to use around strings in Python?


# Fixes:
# 1. Use double quotes
good1 = "I said 'Wow!'"

# 2. Escape the single quotes
good2 = 'I said \'Wow!\''

# 3. Use triple quotes
good3 = '''I said 'Wow!' '''

print(good1, good2, good3)

# Best practice: Most Python developers use single quotes by default and switch to double quotes only if the text itself contains single quotes.
# The key is consistency.