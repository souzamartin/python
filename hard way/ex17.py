# Imports argv module from sys.
from sys import argv
# Imports exists module from ???
from os.path import exists

# Defines argv variables.
script, from_file, to_file = argv

# Prints string containing argv variables
# corresponding to source and output filenames.
print(f"Copying from {from_file} to {to_file}")

# We could do these two on one line. How?
# Defines variable, calling open function on source file specified above.
in_file = open(from_file)
# Defines variable as read function called on open file.
indata = in_file.read()

# Prints string containing length function called on read file.
print(f"The input file is {len(indata)} bytes long")

# Prints string containing exists function check of output file.
print(f"Does the output file exist? {exists(to_file)}")
# Prints string.
print("Ready. Hit RETURN to continue, CTRL-C to abort.")
# Requests input.
input()

# Defines variable, calling open function in write mode
# on output file (which may not exist yet).
out_file = open(to_file, 'w')
# Calls write function on output file,
# writes contents of source file to output file.
out_file.write(indata)

# Prints string.
print("Alright, all done.")

# Closes output and source files.
out_file.close()
in_file.close()
