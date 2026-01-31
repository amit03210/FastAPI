"""
Instructions:
Create a variable called grade and assign it an integer between 0 and 100.
Use if, elif, and else statements to print the letter grade based on the number grade.

Grading Scale:
A → 90 to 100
B → 80 to 89
C → 70 to 79
D → 60 to 69
F → 0 to 59
"""

marks = int(input("Enter the grade \n"))

def evaluate_grade(grade):
    if (grade >= 90 and grade<=100):
        print("Grade is A")
    elif (grade >= 80 and grade<=89):
        print("Grade is B")
    elif (grade >= 70 and grade<=79):
        print("Grade is C")
    elif (grade >= 60 and grade<=69):
        print("Grade is D")
    elif (grade >= 0 and grade<=59):
        print("Grade is F ")
    else:
        print("Enter valid grade")
    
evaluate_grade(marks)

