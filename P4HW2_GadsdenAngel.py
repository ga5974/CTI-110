# Angel Gadsden
# 29 October 2025
# P4HW2
# User inputs employee's name, hours, and rate. Code calculates and outputs inputted info as well as calculated info based on the inputs.

'''
Pseudocode:
Reset total numbers
Get employee name, hours worked, pay rate
Calculate overtime, overtime pay, regular hour pay, gross pay
Display both inputted and calculated info neatly
Loop the process from "get employee name" until user inputs "Done"
Display total of employees inputted, total overpay, regular hours, and grosspay neatly
'''

#reset totals
emp_total = 0
ot_total = 0
reghour_total = 0
gross_total = 0

#input
employee = input("Enter employee's name or 'Done' to terminate: ")

while employee != "Done":
    hours = float(input(f"How many hours did {employee} work? "))
    rate = float(input(f"What is {employee}'s pay rate? "))
    print()
    print(f"Employee name:   {employee}")
    print()
    
    #calculate pay and hours
    if hours>40:
        overtime = float(hours - 40)
        over_pay = overtime * (1.5*rate)
        reghour = (hours-overtime) * rate
        grosspay = over_pay + reghour
    else:
        overtime = 0
        over_pay = 0
        reghour = hours * rate
        grosspay = reghour

    #display
    print("Hours Worked   Pay Rate   OverTime   OverTime Pay        RegHour Pay     Gross Pay")
    print("--------------------------------------------------------------------------------------")
    print(f"{hours:<15.1f}{rate:<11.2f}{overtime:<11.1f}${over_pay:<19.2f}${reghour:<15.2f}${grosspay:.2f}")
    
    #calculate totals
    emp_total += 1
    ot_total += over_pay
    reghour_total += reghour
    gross_total += grosspay
    
    #start next input
    print()
    employee = input("Enter employee's name or 'Done' to terminate: ")
    
#results
print()
print(f"Total number of employees entered: {emp_total}")
print(f"Total amount paid for overtime: ${ot_total}")
print(f"Total amount paid for regular hours: ${reghour_total}")
print(f"Total amount paid in gross: ${gross_total}")