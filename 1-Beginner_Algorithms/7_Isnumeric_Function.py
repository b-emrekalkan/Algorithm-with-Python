
#! PROBLEM: If the two objects received from the user are of an integer typye, write a Python program to sum the two objects.

#? SOLUTION:

xx = input("Please enter a number")

yy = input("Please enter a number")

#* The isnumeric() method 👉 returns True if all the characters are numeric (0-9), otherwise False.

if xx.isnumeric() and yy.isnumeric():
    aa = int(xx) + int(yy)
else:
    aa = "You have not entered a number!"
print(aa)