# Angel Gadsden
# P3LAB
# 16 October 2025
# User inputs money amount, code converts them into and outputs into coin amounts.

#input
amount_float = float(input("Enter a dollar amount with decimals: $"))

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