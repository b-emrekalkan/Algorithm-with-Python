
#! PROBLEM: Write a Python code that separates numbers 1 to 50 as even or odd.

#? SOLUTION-1:

#* The append() method appends an element to the end of the list.

#* Syntax >>> list.append(elmnt)
# elmnt >>> Required. An element of any type (string, number, object etc.)

odds = []

evens = []

for i in range(1,51):
    if i % 2 == 0:
        evens.append(i)
    else:
        odds.append(i)
print(odds)
print(evens)


#? SOLUTION-2:

#* List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

#* Syntax >>> newlist = [expression for item in iterable if condition == True]

odd_numbers = [i for i in range(1,51) if i % 2 == 1]

even_numbers = [i for i in range(1,51) if i % 2 == 0]


#? SOLUTION-3:

print(f"Odd numbers: {[i for i in range(1,51) if i % 2 == 1]}")
print(f"Even numbers: {[i for i in range(1,51) if i % 2 == 0]}")