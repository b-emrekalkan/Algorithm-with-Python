
#! (IN TURKISH) 👉 If there is a strong vowel (a, ı, o, u) in the first syllable of a word, the vowels in other syllables are also thick, and if there is a thin vowel (e, i, ö, ü), the vowels in other syllables will also be thin.

# adım, ayak, boyun, burun, dalga, dudak

# beşik, bilezik, gelincik, gözlük, vergi, yüzük

#? SOLUTION:

name = input("Please enter your name: ").lower()

#* The lower() method returns a string where all characters are lower case.Symbols and Numbers are ignored. 👆

strong_vowel = 0

thick_vowel = 0

for i in name:
    if i in "aıou":
        strong_vowel += 1
    elif i in "eiöü":
        thick_vowel += 1

print(f"Number of Strong Vowel: {strong_vowel}")
print(f"Number of Thick Vowel: {thick_vowel}")

if strong_vowel > 0 or thick_vowel > 0:
    if strong_vowel + thick_vowel == 1:
        result = "Great vowel harmony rule is not sought."
    elif strong_vowel * thick_vowel == 0:
        result = "Follows the rule of great vowel harmony"
    else:
        result = "Doesn't follow the big vowel harmony rule"
else:
    result = "There are no vowels in the word you entered."
print(result)