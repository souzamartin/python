# Imports argv module from sys.
from sys import argv

# Defines arguments for argv.
script, filename = argv

# Prints string containing argv variable specified in CLI.
print(f"We're going to erase {filename}.")
# Prints string containing interrupt instruction.
print("If you don't want that, hit CTRL-C (^C)")
# Prints string containing continue instruction.
print("If you do want that, hit RETURN.")

# Requests input, specifies prompt.
input("?")

# Prints string.
print("Opening the file...")
# Defines variable as file to be opened in write mode.
target = open(filename, 'w')

# Prints string.
print("Truncating the file. Farewell!")
# Calls truncate function on open file specified in variable.
target.truncate()

# Prints string.
print("Now I'm going to ask you for three lines.")

# Three variables defined by input with given prompts.
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# Prints string.
print("I'm going to write these to the file.")

# Six lines call write function on open file specified in variable,
# then write the variables defined by input above, with line breaks.
# Could be reduced to a single write function.
target.write(f"{line1}\n{line2}\n{line3}\n")

# Prints string.
print("And finally, we close it.")
# Closes file specified in variable.
target.close()
