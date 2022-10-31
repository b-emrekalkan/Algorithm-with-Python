
#! Write a function that matches the first number in a sequence with the last number, the second number with the second to last number, and until the numbers run out.

#! If the list is odd length, repeat the middle item twice for the last pair.

#! Return an empty list if the entered is an empty list.

"""
Examples:
(1,2,3,4,5,6,7) 👉 ((1,7),(2,6),(3,5),(4,4))
(1,2,3,4,5,6)   👉 ((1,6), (2,5), (3,4))
( )             👉 ( )
"""

#? SOLUTION:

def pairs(list1):

    list_new = []

    for i in range(len(list1) // 2):
        list_new.append([list1[i], list1[-1-i]])

    if len(list1) % 2 == 1:
        list_new.append([list1[len(list1) // 2], list1[len(list1) // 2]] )
    return list_new

print(pairs([1,2,3,4,5,6]))
print(pairs([1,2,3,4,5,6,7]))