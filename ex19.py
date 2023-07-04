# Defines function 'cheese_and_crackers' with 2 arguments.
# Function prints strings, some containing passed arguments.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man, that's enough for a party!")
    print("Get a blanket.\n")


# Calls function with numerical arguments.
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


# Defines variables, calls function with them.
print("OR we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# Calls function, passes math arguments.
print("We can even do math inside, too:")
cheese_and_crackers(10 + 20, 5 + 6)


# Calls function with variables and math as arguments.
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
