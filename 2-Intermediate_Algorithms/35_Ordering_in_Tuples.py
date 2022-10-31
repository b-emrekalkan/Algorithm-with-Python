
#! Given a list of tuples, implement a method that sort a list in ascending order by the second element inside the tuples and return the list.

# input 👉 [("b",1), ("c",2), ("x",4), ("x",3), ("z",0)]
# output 👉 [("z",0), ("b",1), ("c",2), ("x",3), ("x",4)]

#? SOLUTION-1:

list1 = [("John",1), ("Jade", 2), ("Lisa", 3), ("Rose", 4), ("Louise", 0)]

result = []

for i in range(len(list1)):
    for j in list1:
        if j[1] == i:
            result.append(j)

print(result)


#? SOLUTION-2:

#* A lambda function is a small anonymous function. A lambda function can take any number of arguments, but can only have one expression.

#* Syntax >>> lambda arguments : expression

"""
x = lambda a, b : a * b
print(x(3,5)) # 👉 15

y = lambda a , b=5 : a * b
print(y(3)) # 👉 15
"""


print(sorted(list1, key = lambda x : x[1]))