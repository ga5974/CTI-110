# Angel Gadsden
# 2 October 2025
# P2HW2
# User inputs grades, code puts grades in a list and outputs the lowest & highest grade, the sum of the grades, and the average of the grades.

a= float(input("Enter grade for Module 1: "))
b= float(input("Enter grade for Module 2: "))
c= float(input("Enter grade for Module 3: "))
d= float(input("Enter grade for Module 4: "))
e= float(input("Enter grade for Module 5: "))
f= float(input("Enter grade for Module 6: "))

grades= [a, b, c, d, e, f]
grades.sort()
total= sum(grades)
average= total/6

print()
print("---------- Results ----------")
print(f"Lowest Grade:        {grades[0]}")
print(f"Highest Grade:       {grades[5]}")
print(f"Sum of Grades:       {total}")
print(f"Average:             {average:.2f}")
print("-----------------------------")