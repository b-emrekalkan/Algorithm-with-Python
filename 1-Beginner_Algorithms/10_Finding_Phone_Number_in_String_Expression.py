
#! PROBLEM: Write python code that extracts the phone number in a given string expression.

# given_str = "My phone number is (111) 222-33-44"
# output = 1112223344

#? SOLUTION:

given_str = "My phone number is (111) 222-33-44"

output = ""

for i in given_str:
    if i in "0123456789": # or we can use 👉 if i.isnumeric():
        output += i
print(output)