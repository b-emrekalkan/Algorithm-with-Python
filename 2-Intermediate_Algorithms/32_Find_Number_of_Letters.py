
#! Take a sentence from the user and find the number of alphabetic characters.

# input >> "Hello World!"

# output >> [('H', 1), ('e', 1), ('l', 3), ('o', 2), ('W', 1), ('r', 1), ('d', 1)]

# output >> {'H': 1, 'e': 1, 'l': 3, 'o': 2, 'W': 1, 'r': 1, 'd': 1}

#? SOLUTION-1:

sentence = input("Enter a sentence: ")

my_list = []

for i in sentence:
    if i.isalpha():
        my_list.append(i)

result = []

for i in range(len(my_list)):
    if (my_list[i], my_list.count(my_list[i])) not in result:
        result.append((my_list[i], my_list.count(my_list[i])))

print(result)


#? SOLUTION-2:

sent = input("Enter a sentence: ")

my_dict = dict()

for i in sent:
    if i.isalpha():
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1

print(my_dict)