
#! Create an algorithm that keeps the odd numbers sequentially and the even numbers in their original positions in given array.

""" Examples:
(7,1) >> (1,7)
(5,8,6,3,4) >> (3,8,6,5,4) """

#? SOLUTION:

#* The sorted() function returns a sorted list of the specified iterable object. You can specify ascending or descending order. Strings are sorted alphabetically, and numbers are sorted numerically.

#* Note: You cannot sort a list that contains BOTH string values AND numeric values.

#* Syntax >> sorted(iterable, key=key, reverse=reverse)
"""
 iterable >> 	Required. The sequence to sort, list, dictionary, tuple etc.
 key      >> 	Optional. A Function to execute to decide the order. Default is None
 reverse  >>  	Optional. A Boolean. False will sort ascending, True will sort descending. Default is False
"""

def asc(list1):
    odd = [i for i in list1 if i % 2]
    odd = sorted(odd)

    k= 0
    result = []

    for i in list1:
        if i % 2:
            result.append(odd[k])
            k += 1
        else:
            result.append(i)
    return result

print(asc([5,8,6,3,4]))