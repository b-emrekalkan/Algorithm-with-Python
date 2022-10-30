
#! PROBLEM: Take a word from the user and create an algorithm that repeats the process starting from the first letter of that word, one letter at a time, up to the last letter, capitalized, and outputs the results in a list.

# Example >> (Joseph, jOseph, joSeph, josEph, josePh, josepH)

#? SOLUTION:

#* The lower() method 👉 returns a string where all characters are lower case. Symbols and Numbers are ignored!! 👇

#* The upper() method 👉 returns a string where all characters are in upper case.Symbols and Numbers are ignored.

#* The range() function 👉 returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number. >>> range(start, stop, step) 👇

word = input("Please enter a word: ").lower()

result = []

for i in range(len(word)):
    result.append(word[:i] + word[i].upper() + word[i+1:])