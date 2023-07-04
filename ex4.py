# defines number of cars
cars = 100
# defines passenger capacity of each car
space_in_a_car = 4.0
# defines number of drivers
drivers = 30
# defines number of passengers
passengers = 90
# defines number of unused cars in terms of total number of cars and drivers
cars_not_driven = cars - drivers
# defines number of cars driven as number of drivers
cars_driven = drivers
# defines total carpool capacity in terms of cars driven and car capacity
carpool_capacity = cars_driven * space_in_a_car
# defines average number of passengers per car
# in terms of total passengers and cars driven
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
