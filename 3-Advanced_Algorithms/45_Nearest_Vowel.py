
#! Given a letter, create a function that returns the vowel closest to the letter. If two vowels are equidistant from the given letter, return the previous vowel.

"""
Example:

nearest_vowel("s") 👉 "u"
nearest_vowel("c") 👉 "a"
nearest_vowel("i") 👉 "i"
"""

#? SOLUTION:

def nearest_vowel(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    vowels_index = [ alphabet.index(i) for i in "aeiou"] # [0,4,8,14,20]

    nearest = [abs(alphabet.index(letter) - i) for i in vowels_index]

    return "aeiou"[nearest.index(min(nearest))]

print(nearest_vowel("s"))