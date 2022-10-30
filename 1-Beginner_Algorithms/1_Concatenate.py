
#! PROBLEM: Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.

#? SOLUTION:

s1 = "yellow"
s2 = "joseph"

#* The len() function 👉 returns the number of items in an object. When the object is a string, the len() function returns the number of characters in the string. 👇

#* The print() function 👉 prints the specified message to the screen, or other standard output device. The message can be a string, or any other object, the object will be converted into a string before written to the screen. 👇

s3 = s1[:len(s1) // 2] + s2 + s1[len(s1) // 2:]
print(s3)