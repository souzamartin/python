# Imports argv module.
from sys import argv
# read the WYSS section for how to run this
# Specifies variables which must be supplied to argv in CLI.
script, first, second, third = argv

# Prints variables defined by input in CLI.
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
