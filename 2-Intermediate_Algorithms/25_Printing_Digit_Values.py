
#! Write a Python code that returns the digits value of the given number in a list.

""" Examples:
-153 >> [-100,-50,-3] >> [-(1 * (10 ** 2)), -(5 * (10 ** 1)), -(3 * (10 ** 0))]

2022 >> [2000,0,20,2]"""


#? SOLUTION-1:

def num_split(num):

    count = 0
    result = []

    for i in str(abs(num))[::-1]:
        result.append(int(i) * 10 ** count )
        count += 1

    result2 = []

    if num < 0:
        for i in result[::-1]:
                result2.append(-i)
    else:
        result2 = result[::-1]

    return result2

print(num_split(-153))



#? SOLUTION-2:

def num_split2(num):

    count = 0
    result = []

    for i in str(abs(num))[::-1]:
        result.append(int(i) * 10 ** count )
        count += 1

    return result[::-1] if num >=0 else [-i for i in result[::-1]]

print(num_split(-153))