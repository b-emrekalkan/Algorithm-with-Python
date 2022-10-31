
#! Write a functin scramble(str1, str2) that returns true if some of the str1 characters can be rearranged to match str2, false otherwise.

#! NOTE >> Only lower case letters will be used (a-z). No punctuation or digits will be included.

"""
Examples:
scramble("rkqodlw", "world") ==> True
scramble("katas", "steak") ==> False
"""

#? SOLUTION-1:

def scramble(str1, str2):

    a = set(str1)

    count = 0

    for i in str2:
        if i in a:
            count += 1
    if count == len(str2):
        return True
    else:
        return False

print(scramble("datascientist", "sedat"))  # 👉 True


#? SOLUTION-2:

#* The issubset() method 👉 returns True if all items in the set exists in the specified set, otherwise it retuns False.

#* Syntax >>>> set.issubset(set)

#* set >>>	Required. The set to search for equal items in

def scramble1(str1,str2):

    a1 = {i for i in str1 for j in str2 if set(i).issubset(j)}

    return len(a1) == len(str2)

print(scramble1("datascientist", "sedat"))  # 👉 True
