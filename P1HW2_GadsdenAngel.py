# Angel Gadsden
# 18 September 2025
# P1HW2
# User inputs their budget, destination, and how much they will spend on necessities for their trip.

#Pseudocode:
#Get budget
#Get destination
#Get gas
#Get hotel
#Get food
#Add expenses
#Budget - Expenses = Result
#Display result

print()
print("--- This program calculates and displays travel expenses! ---")
print()
budget= int(input("Enter your budget: "))
print()
destination= input("Enter your travel destination: ")
print()
gas= int(input("How much do you think you will spend on gas? "))
print()
hotel= int(input("Approximately, how much will you need for accomodation/hotel? "))
print()
food= int(input("Lastly, how much do you need for food? "))
expenses= gas+hotel+food
print()
print()
print("--- Travel Expenses ---")
result= budget-expenses
print()
print("Location: ", destination)
print("Inital Budget: ", budget)
print()
print("Fuel: ", gas)
print("Accomodation: ", hotel)
print("Food: ", food)
print()
print("Remaining Balance: ", result)
print()

