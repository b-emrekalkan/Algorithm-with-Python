
#! PROBLEM: Write a program to find how many times substring "Mr.Bean" appears in the given string.
# str_x = "Mr.Bean is good actor and Mr.Bean is very funny."

#? SOLUTION:

str_x = "Mr.Bean is good actor and Mr.Bean is very funny."

#* The count() method 👉 returns the number of times a specified value appears in the string. 👇

a = str_x.count("Mr.Bean")

print(f"Mr.Bean appeared {a} times.")

#* The format() method 👉 formats the specified value(s) and insert them inside the string's placeholder 👇

print("Mr.Bean appeared {} times.".format(a))