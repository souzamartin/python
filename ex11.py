# Prints string, specifies not to end with newline.
print("How old are you?", end=' ')
# Requests input to define variable.
age = input()
# As above.
print("How tall are you?", end=' ')
# As above.
height = input()
# As above.
print("How much do you weigh?", end=' ')
# As above.
weight = input()

# Prints string containing variables defined by inputs above.
print(f"So, you're {age} old, {height} tall, and {weight} heavy.")
