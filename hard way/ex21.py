# Defines function to add two arguments, return result.
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

# Defines function to subtract two arguments, return result.
def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

# Defines function to multiply two arguments, return result.
def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

# Defines function to divide two arguments, return result.
def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions!")

# Variables defined with values returned from each called function.
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

# Prints string with results returned from functions.
print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for extra credit. Type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")
