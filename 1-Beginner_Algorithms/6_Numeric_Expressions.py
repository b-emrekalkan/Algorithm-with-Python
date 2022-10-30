
#! PROBLEM: Create an algorithm that will return True if the two integer values you get from the user are equal or the difference of these numbers is a multiple of 5.

#? SOLUTION - 1:

x = int(input("Enter a number"))
y = int(input("Enter a number"))

#* The abs() function 👉 returns the absolute value of the specified number 👇

if x == y or abs(x-y) % 5 == 0:
    print("True")
else:
    print("False")

#? SOLUTION - 2:

a = int(input("Enter a number"))
b = int(input("Enter a number"))

print(x == y or abs(x-y) % 5 == 0)