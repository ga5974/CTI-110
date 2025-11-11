# Angel Gadsden
# P5LAB
# 11 November 2025
# Program outputs random dollar amount, user inputs dollar amount. Program calculates change amount and, using the disperse_change function, outputs the dollar+coin amounts.

#importing
import random
random_num = round(random.uniform(0.01, 100.00), 2)

#function (P3LAB)
def disperse_change():
    if (amount_float == 0):
        print("No change.")

    #conversion
    amount = int(amount_float *100)

    dollars = amount // 100
    amount = amount - (dollars*100)

    quarters= amount // 25
    amount = amount - (quarters*25)

    dimes= amount // 10
    amount = amount - (dimes*10)

    nickels= amount // 5
    amount = amount - (nickels*5)

    pennies = amount

    #display
    if dollars > 0:
        if dollars == 1:
            print(f"{dollars} Dollar")
        else: print(f"{dollars} Dollars")

    if quarters > 0:
        if quarters == 1:
            print(f"{quarters} Quarter")
        else: print(f"{quarters} Quarters")

    if dimes > 0:
        if dimes == 1:
            print(f"{dimes} Dime")
        else: print(f"{dimes} Dimes")

    if nickels > 0:
        if nickels == 1:
            print(f"{nickels} Nickel")
        else: print(f"{nickels} Nickels")

    if pennies > 0:
        if pennies == 1:
            print(f"{pennies} Penny")
        else: print(f"{pennies} Pennies")

#random num + input
print(f"You owe ${random_num}.")
cash = float(input("How much cash will you put in the self-checkout? $"))

#change
amount_float = cash - random_num
print(f"Change is: ${amount_float:.2f}")
print()
disperse_change()



