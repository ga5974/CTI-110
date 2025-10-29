# Angel Gadsden
# 29 October 2025
# P4HW1
# User inputs how many grades they'll input, code outputs input prompts then calculates the lowest, average, and average letter grade. Code also provides a modified list without the minimum grade.

'''
Psuedocode:
User inputs how much grade scores they want to input
Code creates an empty list and prompts them to fill out scores within the amount asked
If anything below zero is entered, it is invalid and the user is prompted to reenter the score
Add inputted grades to list
Determine the lowest grade
Copy the list and remove lowest grade from list
Determine average from list
Determine letter grade based on average
Display lowest grade, the modified list, the average, and letter grade neatly
'''



#input
scores_am= int(input("How many scores do you want to enter? "))
print()

#list creation
grades_list = []

#loop
num_scores = 0
while num_scores < scores_am:
    score = float(input(f"Enter Score #{num_scores+1}: "))
    while score < 0 or score > 100:
        print("INVALID Score entered!")
        print("Score should be between 0 and 100.")
        print()
        score = float(input(f"Enter Score #{num_scores+1} again: "))
    grades_list.append(score)
    num_scores += 1

#calculations/list copying
lowest = min(grades_list)
mod_list = grades_list.copy()
mod_list.remove(lowest)
average = sum(mod_list) / len(mod_list)

if average >= 90:
    avg_grade = "A"
elif average >= 80:
    avg_grade = "B"
elif average >= 70:
    avg_grade = "C"
elif average >= 60:
    avg_grade = "D"
else:
    avg_grade = "F"

#results
print()
print("---------- Results ----------")
print(f"Lowest Grade   :   {lowest}")
print(f"Modified List  :   {mod_list}")
print(f"Scores Average :   {average:.2f}")
print(f"Grade          :   {avg_grade}")
print("-----------------------------")
