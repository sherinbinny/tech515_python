import sys

# check for arguments
if len(sys.argv) > 1:
    print("You gave me an argument!")
else:
    print("You gave me no arguments!")

print(type(sys.argv))
print(sys.argv[0])
print(sys.argv[1])
print(sys.argv[2])
