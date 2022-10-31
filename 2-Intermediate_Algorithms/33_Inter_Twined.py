
#! Given two arrays -list1 and list2- construct an algorithm that returns the elements of list1 which are subarrays of list2.

""" Example:

list1 = ["old", "int", "age", "and"]
list2 = ["random", "soldier", "list", "print"]
returns >>> ["old", "int", "and"] """


#? SOLUTION-1:

def intertwined(list1,list2):

    new_list = []

    for i in list2:
        for j in list1:
            if j in i and j not in new_list:
                new_list.append(j)
    return new_list

print(intertwined(["old", "int", "age", "and"], ["random", "soldier", "list", "print"]))


#? SOLUTION-2:

#* The set() function creates a set object. The items in a set list are unordered, so it will appear in random order.

#* Syntax >>> set(iterable)


def intertwinedd(list1,list2):

    return list(set([j for i in list2 for j in list1 if j in i]))

print(intertwinedd(["old", "int", "age", "and"], ["random", "soldier", "list", "print"]))

