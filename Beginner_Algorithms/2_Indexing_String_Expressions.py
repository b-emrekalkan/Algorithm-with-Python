
#! PROBLEM: Write a Python program to return a string consisting of the first 3 and last 3 characters of a string you received from user. If string length is less than 3, return "empty string".

#? SOLUTION:

#* The input() function 👉 allows user input. 👇

company = input("Please enter your company:")

if len(company) >= 3:
    #* first 3 characters + last 3 characters 👇
    print(company[:3] + company[-3:])
else:
    print("empty string")