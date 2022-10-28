#! PROBLEM: Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.

#? SOLUTION:

s1 = "yellow"
s2 = "joseph"

#* The len() function 👉 returns the number of items in an object. When the object is a string, the len() function returns the number of characters in the string. 👇

#* The print() function 👉 prints the specified message to the screen, or other standard output device. The message can be a string, or any other object, the object will be converted into a string before written to the screen. 👇

s3 = s1[:len(s1) // 2] + s2 + s1[len(s1) // 2:]
print(s3)


#! PROBLEM: Write a Python program to return a string consisting of the first 3 and last 3 characters of a string you received from user. If string length is less than 3, return "empty string".

#? SOLUTION:

#* The input() function 👉 allows user input. 👇

company = input("Please enter your company:")

if len(company) >= 3:
    #* first 3 characters + last 3 characters 👇
    print(company[:3] + company[-3:])
else:
    print("empty string")

#! PROBLEM: Write a program to find how many times substring "Mr.Bean" appears in the given string.
# str_x = "Mr.Bean is good actor and Mr.Bean is very funny."

#? SOLUTION:

str_x = "Mr.Bean is good actor and Mr.Bean is very funny."

#* The count() method 👉 returns the number of times a specified value appears in the string. 👇

a = str_x.count("Mr.Bean")

print(f"Mr.Bean appeared {a} times.")

#* The format() method 👉 formats the specified value(s) and insert them inside the string's placeholder 👇

print("Mr.Bean appeared {} times.".format(a))


#! PROBLEM: Write a program to display your details like name, age, job in three different lines.

#? SOLUTION:

#* The split() method 👉 splits a string into a list. You can specify the separator, default separator is any whitespace. 👇

per = input("Please enter your name, age and job seperating them with comma").split(",")

#* If you see this character ("\n") in a string, that means that the current line ends at that point and a new line starts right after it 👇

print(f"name: {per[0]}\nage: {per[1]}\njob: {per[2]}")


#! PROBLEM: Create an algorithm that asks the employee for weekly working hours and hourly wage information and ultimately calculates the employee's weekly salary.
# Note >> Work over 40 hours per week is paid 1.5 times the wage

#? SOLUTION:

#* The int() function 👉 converts the specified value into an integer number. 👇

work_hours = int(input("Please enter your weekly working hour:"))

hourly_wage = int(input("Please enter your hourly wage:"))

if work_hours > 40:
    weekly_wage = (work_hours - 40) * (1.5 * hourly_wage) + 40 * hourly_wage
else:
    weekly_wage = work_hours * hourly_wage
print(f"Your weekly wage is {weekly_wage}")


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


#! PROBLEM: Write a program that takes a country's name and its area as arguments and returns the area of the country's proportion of the total world's landmass.
# The total world's landmass is 148,940,000 (km ** 2)

#? SOLUTION:

country = input("Enter country name")
area = input("Enter the area of the country")
earth = 148940000

#* The round() function 👉 returns a floating point number that is a rounded version of the specified number, with the specified number of decimals. The default number of decimals is 0, meaning that the function will return the nearest integer 👇

percentile = round((int(area) / earth) * 100,2)

print(f"{country} is {percentile}% of the total world's landmass")


#! PROBLEM: Create an algorithm that finds BMI.

#? SOLUTION:

weight = int(input("Please enter your weight in kg:"))
height = int(input("Please enter your height in cm"))

result = round(weight / ((height / 100) ** 2),2)

if result < 18.5:
    body = "underweight"
elif result < 25:
    body = "normal"
elif result < 30:
    body = "overweight"
elif result < 35:
    body = "obese"
else:
    body = "extremely obese"
print(f"Your BMI is: {result} and your body type is: {body}")


#! PROBLEM: Write python code that extracts the phone number in a given string expression.

# given_str = "My phone number is (111) 222-33-44"
# output = 1112223344

#? SOLUTION - 1:

given_str = "My phone number is (111) 222-33-44"

output = ""

for i in given_str:
    if i in "0123456789": # or we can use 👉 if i.isnumeric():
        output += i
print(output)


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


#! PROBLEM: Take a word from the user and create an algorithm that repeats the process starting from the first letter of that word, one letter at a time, up to the last letter, capitalized, and outputs the results in a list.

# Example >> (Joseph, jOseph, joSeph, josEph, josePh, josepH)

#? SOLUTION:

#* The lower() method 👉 returns a string where all characters are lower case. Symbols and Numbers are ignored!! 👇

#* The upper() method 👉 returns a string where all characters are in upper case.Symbols and Numbers are ignored.

#* The range() function 👉 returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number. >>> range(start, stop, step) 👇

word = input("Please enter a word: ").lower()

result = []

for i in range(len(word)):
    result.append(word[:i] + word[i].upper() + word[i+1:])