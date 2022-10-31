
#! Create an algorithm that prints numbers greater than the next number.

"""
Examples:
[3,13,11,2,1,9,5] >>> [13,11,9,5]
[5,5,5,5] >>> [5]
"""

#? SOLUTION:

#* The max() function returns the item with the highest value, or the item with the highest value in an iterable. If the values are strings, an alphabetically comparison is done.

#* Syntax >>> max(n1, n2, n3, ...) or max(iterable)

list1 = [3,13,11,2,1,9,5]

list2 = []
for i in range(0, len(list1)):
    if list1[i] < max(list1[i:]):
        list2.append(list1[i])

other = {i for i in list1 if i not in list2}
print(sorted(list(other), reverse = True))