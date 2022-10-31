
#! Write a program that checks if a sentence is Palindrome.

#? SOLUTION:

#* The join() method takes all items in an iterable and joins them into one string. A string must be specified as the separator.

#* Syntax >>> string.join(iterable)

#* The isalpha() method returns True if all the characters are alphabet letters (a-z). Example of characters that are not alphabet letters: (space)!#%&? etc.

#* Syntax >>> string.isalpha()

"".join(i.lower() for i in "AbC12" if i.isalpha()) # abc


sentence = input("Enter a sentence: ")

edit_sentence = "".join(i.lower() for i in sentence if i.isalpha())

if edit_sentence == edit_sentence[::-1]:
    print(f"{sentence} is Palindrome.")
else:
    print(f"{sentence} is not Palindrome.")