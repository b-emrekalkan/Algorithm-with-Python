
#! PROBLEM: Ask the user for the grade she/he got from the exam and print the letter grate corresponding to her/his grade.

#? SOLUTION:

score = int(input("Please enter your score: "))

if 0 <= score <= 100:
    if score >= 80:
        result = "A"
    elif score >= 65:
        result = "B"
    elif score >= 55:
        result = "C"
    elif score >= 50:
        result = "D"
    elif score < 50:
        result = "F"
    print(f"Your letter score is {result}")
else:
    print("Invalid input!")