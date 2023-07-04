# Imports argv module.
from sys import argv

# Specifies argv variables.
script, filename = argv

# Defines variable in terms of calling open function
# on file with filename specified in CLI.
txt = open(filename)

# Prints string containing specified filename.
print(f"Here's your file {filename}:")
# Prints contents of file named in variable txt
# by giving command .read.
print(txt.read())

# Closes the file.
txt.close()

# Repeats the above with new variables, this time
# asking user to specify the filename with input function.
# This can open and read a different file.
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

txt_again.close()
