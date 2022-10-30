
#! PROBLEM: Assume a long string containing more than one word and reverse it word by word.


#? SOLUTION-1:

#* The split() method splits a string into a list. You can specify the separator, default separator is any whitespace.

#* Note: When maxsplit is specified, the list will contain the specified number of elements plus one.

#* Syntax >>> string.split(separator, maxsplit)

# separator >>>	Optional. Specifies the separator to use when splitting the string. By default any whitespace is a separator

# maxsplit >>>	Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"

name = "My name is Emre and I'm 32 years old"

word_list = name.split(" ") # ['My', 'name', 'is', 'Emre', 'and', "I'm", '32', 'years', 'old']

n = len(word_list) - 1

while n >= 0:
    #* end='end' >>> Optional Parameter >= Specify what to print at the end. Default is '\n' (line feed) 👇

    print(word_list[n], end = " ")
    n -= 1

#? SOLUTION-2:

new_name = "My name is Emre and I'm 32 years old"

new_list = name.split(" ")

print(*new_list[::-1])

#! * symbol is use to print the list elements in a single line with space. 👆