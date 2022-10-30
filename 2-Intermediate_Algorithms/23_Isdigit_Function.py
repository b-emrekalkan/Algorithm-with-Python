
#! Create an algorithm that if the place value of the number you get from the user is:
#! less than 3, print the square of the number instead.
#! If greater than 3 and odd; print the 2 less of the number instead.
#! If greater than 3 and even; print the 1 more of the number instead.
#! If no valid value is entered; print "Invalid input!".


#? SOLUTION:

x = input("Please enter a number: ")

result = ""

if x.isdigit():
    for i in x:
        if int(i) <= 3:
            result += str(int(i) ** 2)
        elif int(i) % 2:
            result += str(int(i) - 2)
        else:
            result += str(int(i) + 1)
else:
    print("Invalid input!")

print(result)

# For "12345" 👉 14953