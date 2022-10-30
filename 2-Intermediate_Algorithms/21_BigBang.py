
#! PROBLEM: Write a Python program which iterates the integers from 1 to 50. For multiples of three; print "Big" instead of the number and for the multiples of seven; print "Bang". For numbers which are multiples of both three and seven; print "BigBang".


#? SOLUTION:

for i in range(1,51):
    if i % 3 == 0 and i % 7 == 0:
        print("BigBang")
    elif i % 3 == 0:
        print("Big")
    elif i % 7 == 0:
        print("Bang")
    else:
        print(i)