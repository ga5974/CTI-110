# Angel Gadsden
# 16 October 2025
# P3HW2
# User inputs employee's name, hours, and rate. Code calculates and outputs inputted info as well as calculated info based on the inputs.

'''
Pseudocode:
Get employee name
Get hours worked
Get employee pay rate
Calculate overtime
Calculate overtime pay
Calculate regular hour pay
Calculate gross pay
Display both inputted and calculated info neatly
'''

#input
employee = input("Enter employee's name: ")
hours = float(input("Number of hours worked: "))
rate = float(input("Enter employee's pay rate: "))
print("-----------------------------------------")
print(f"Employee name:   {employee}")
print()

#calculate
overtime = float(hours - 40)
over_pay = overtime * (1.5*rate)
reghour = (hours-overtime) * rate
grosspay = over_pay + reghour

#display
print("Hours Worked   Pay Rate   OverTime   OverTime Pay        RegHour Pay     Gross Pay")
print("--------------------------------------------------------------------------------------")
print(f"{hours:<15.1f}{rate:<11.1f}{overtime:<11.1f}${over_pay:<19.2f}${reghour:<15.2f}${grosspay:.2f}")