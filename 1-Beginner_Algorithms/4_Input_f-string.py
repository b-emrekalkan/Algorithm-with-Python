
#! PROBLEM: Write a program to display your details like name, age, job in three different lines.

#? SOLUTION:

#* The split() method 👉 splits a string into a list. You can specify the separator, default separator is any whitespace. 👇

per = input("Please enter your name, age and job seperating them with comma").split(",")

#* If you see this character ("\n") in a string, that means that the current line ends at that point and a new line starts right after it 👇

print(f"name: {per[0]}\nage: {per[1]}\njob: {per[2]}")