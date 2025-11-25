import sys

# gives us the current paths important to the Python interpreter
print(f"Current path: {sys.path}")

print(sys.version)

import datetime

# gives us today's date
print(f"Today's date: {datetime.date.today()}")

import builtins

for name in dir(builtins):
    if name[0].islower():
        print(name)
