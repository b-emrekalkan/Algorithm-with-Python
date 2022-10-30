
#! PROBLEM: Imagine a circle and two squares inside and outside the circle. Create a program that takes an integer (radius of the circle) and return the difference of the areas of two squares.

# Radius = 5 ==> Output >> 50
# Radius = 6 ==> Output >> 72

#? SOLUTION:

r = int(input("Please enter r value"))

out_square = (2 * r) ** 2

inner_square = (r ** 2) * 2


diff_square = ((2 * r) ** 2 - (r ** 2) * 2)

print(f"The difference is {diff_square}")