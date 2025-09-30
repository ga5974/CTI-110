#Angel Gadsden
#23 September 2025
#P2LAB2
#User inputs vehicle, code outputs its mpg, user inputs gallons, code then calculates and outputs miles based on gallons and mpg.

cars = {
    "Camero": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26,
}
keys = cars.keys()
print(keys)
print()
car_name= input("Enter a vehicle to see its mpg: ")
mpg= cars[car_name]
print()
print(f"The {car_name} gets {mpg} mpg.")
print()
miles = int(input(f"How many miles will you drive the {car_name}? "))
total= miles/mpg
print()
print(f"{total:.2f} gallon(s) of gas are needed to drive the {car_name} {miles:.1f} miles.")
