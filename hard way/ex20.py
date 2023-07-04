# Imports argv module.
from sys import argv

# Defines argv arguments.
script, input_file = argv

# Defines function to print entire contents of file.
def print_all(f):
    print(f.read())

# Defines function to return virtual read head
# to start of file.
def rewind(f):
    f.seek(0)

# Defines function to print single line from file.
def print_a_line(line_count, f):
    print(line_count, f.readline())

# Defines variable 'current_file' as file specified
# by argv argument.
current_file = open(input_file)

print("First let's print the whole file:\n")

# Calls function to print entire contents of open file.
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# Calls function to return to start of open file.
rewind(current_file)

print("Let's print three lines:")

# Defines variable (1).
current_line = 1
# Calls function to print single line of open file.
print_a_line(current_line, current_file)

# Defines variable again with advance of 1 (2).
current_line += 1
# Calls function again to print single line
# with updated variable.
print_a_line(current_line, current_file)

# Defines variable again with another advance of 1 (3).
current_line += 1
# Calls function again with updated variable.
print_a_line(current_line, current_file)
