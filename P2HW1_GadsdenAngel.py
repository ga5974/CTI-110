# Angel Gadsden
# 2 October 2025
# P2HW1
# User inputs their budget, destination, and how much they will spend on necessities for their trip. - Now better formatted!

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
print("--------- Travel Expenses ---------")
result= budget-expenses
print()
print(f"Location:          {destination}")
print(f"Inital Budget:     ${budget:>.2f}")
print(f"Fuel:              ${gas:>.2f}")
print(f"Accomodation:      ${hotel:>.2f}")
print(f"Food:              ${food:>.2f}")
print("-----------------------------------")
print()
print(f"Remaining Balance: ${result:>.2f}")
print()

