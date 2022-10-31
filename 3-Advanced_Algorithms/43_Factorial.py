
#! Write a Python code that calculates the factorial of the given number.

"""
Example:

4 ---->> 24 (4*3*2*1)
6 ---->> 720 (6*5*4*3*2*1)
 """

 #? SOLUTION-1 (WITH WHILE):

def fact(x):

    mult = 1
    while x > 0:
        mult *= x
        x -= 1

    return mult

print(fact(6))


 #? SOLUTION-2 (WITH FOR):

def fact2(x):

    mult2 = 1
    for i in range(x,0,-1):
        mult2 *= i

    return mult2

print(fact2(5))


#? SOLUTION-3 (WITH RECURSIVE FUNCTION):

def fact3(x):
    if x == 1:
        return 1
    else:
        return x * fact3(x - 1)

print(fact3(4))