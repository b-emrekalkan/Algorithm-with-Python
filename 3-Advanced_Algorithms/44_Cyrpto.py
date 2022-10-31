
#! alphabet = "abcçdefgğhıijklmnoöprsştuüvyz"

#! Create an algorithm that encodes a sentence or word you receive from the user so that the first letter is the 7th letter of the alphabet and outputs it.

"""
Example:

Joseph >>> Ötyiüm
Mr.Bean >> Sv.Gifş
"""

#? SOLUTION:

#* The isupper() method 👉 returns True if all the characters are in upper case, otherwise False. Numbers, symbols and spaces are not checked, only alphabet characters.

#* Syntax >>> string.isupper()

#* The islower() method returns True if all the characters are in lower case, otherwise False. Numbers, symbols and spaces are not checked, only alphabet characters.

#* Syntax >>> string.islower()

#* The upper() method returns a string where all characters are in upper case. Symbols and Numbers are ignored.

#* Syntax >>> string.upper()


word = input("Please enter a sentence or word: ")

def cyrpto(word):
    alphabet = "abcçdefgğhıijklmnoöprsştuüvyz"
    rot_7 = "fgğhıijklmnoöprsştuüvyzabcçde"

    new = ""
    for i in word:
        if i.isupper():
            new += (rot_7[alphabet.index(i.lower())]).upper()
        elif i.islower():
            new += rot_7[alphabet.index(i)]
        else:
            new += i
    return new

print(cyrpto(word))