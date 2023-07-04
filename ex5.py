name = 'Martin Souza'
age = 35 # coincidentally not a lie
height = 5 * 12 + 1 # inches
height_metric = height * 2.54
weight = 140 # lbs
weight_metric = weight * 0.453592
eyes = 'Hazel'
teeth = 'Yellowish'
hair = 'Dark brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"That's {height_metric} centimeters tall.")
print(f"He's {weight} pounds heavy.")
print(f"Or, if you prefer, {weight_metric} kilos heavy.")
print("Actually that's not too heavy, either way.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
