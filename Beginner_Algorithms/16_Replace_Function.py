
#! PROBLEM: Write a code that replacet the first character of a string given to you or received from the user, without changing the first character, with a "?" sign.

# input >>> restart
# output >> resta?t

#? SOLUTION-1:

text = "restart"

new_text = text[0]

for i in range(1, len(text)):
    if text[i] == text[0]:
        new_text += "?"
    else:
        new_text += text[i]
print(new_text)


#? SOLUTION-2:

#* The replace() method replaces a specified phrase with another specified phrase. All occurrences of the specified phrase will be replaced, if nothing else is specified.

#* Syntax >>> string.replace(oldvalue, newvalue, count) 👇
# oldvalue >>>	Required. The string to search for
# newvalue >>>	Required. The string to replace the old value with
# count    >>>	Optional. A number specifying how many occurrences of the old value you want to replace. Default is all occurrences

x = input("Enter a word: ")

x_new = x.replace(x[0], "?")[1:]

print(x[0] + x_new)