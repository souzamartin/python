# defines variable
types_of_people = 10
# defines variable as an f-string containing a different, nested variable
x = f"There are {types_of_people} types of people."

# defines variable
binary = "binary"
# defines variable
do_not = "don't"
# defines variable as an f-string containing two other nested variables
y = f"Those who know {binary} and those who {do_not}."

# prints variable
print(x)
# prints variable
print(y)

# prints f-string containing variable
print(f"I said: {x}")
# prints f-string containing variable
print(f"I also said: '{y}'")

# defines variables
hilarious = False
# defines variable as string with anchor point for nested variable
joke_evaluation = "Isn't that joke so funny?! {}"

# prints variable, inserts formatted nested variable
print(joke_evaluation.format(hilarious))

# defines variable as string
w = "This is the left side of... "
# defines variable as string
e = "a string with a right side."

# prints two variables together
print(w + e)
