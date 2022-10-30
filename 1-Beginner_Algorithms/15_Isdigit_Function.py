
#! PROBLEM: Write a Python program that accepts a figure (n) and computes the value of n+nn+nnn.

# input >>> 5
# output >> (5+55+555) >>> 615

#? SOLUTION:

#* The isdigit() method returns True if all the characters are digits, otherwise False. Exponents, like ², are also considered to be a digit.

#* Syntax >>> string.isdigit()

a = input("Enter a figure: ")

if a.isdigit():
    if int(a) in [0,1,2,3,4,5,6,7,8,9]:
        result = int(a) + int(a * 2) + int(a * 3)
    else:
        result = "Make sure you enter a figure"
else:
    result = "Make sure you enter a figure"
print(result)


# Output for "6" 👉 738
