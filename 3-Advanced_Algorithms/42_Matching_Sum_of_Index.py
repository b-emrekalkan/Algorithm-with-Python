
#! Given a list and a targer number, write a Python code that specifies which two elements of the list can reach that number.

"""
Example:

[2,8,9,15,5,12], target_num = 17 => 👇
[[0,3],[1,2],[2,1],[3,0], [4,5], [5,4]]
"""

#? SOLUTION-1:

#* The index() method returns the position at the first occurrence of the specified value.

#* Syntax >>> list.index(elmnt)

#* elmnt >>>  Required. Any type (string, number, list, etc.). The element to search for


def target(list1, target_num):

    a= []
    b= []

    for i in list1:
        for j in list1:
            if i + j == target_num:
                a.append(list1.index(i))
                b.append(list1.index(j))

    k = 0
    while k < len(a):
        print(f"{a[k]} and {b[k]}")
        k += 1

print(target([2,8,9,15,5,12], 17))


#? SOLUTION-2:

def targett(list1, target_num):

    a= []

    for i in list1:
        for j in list1:
            if i + j == target_num:
                a.append([list1.index(i), list1.index(j)])
    return a

print(targett([2,8,9,15,5,12], 17))


#? SOLUTION-3:

def targettt(list1, target_num):

    return [[list1.index(i), list1.index(j)] for i in list1 for j in list1 if i + j == target_num]

print(targettt([2,8,9,15,5,12], 17))