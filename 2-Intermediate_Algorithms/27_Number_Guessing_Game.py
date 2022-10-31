
#! Number Guessing Game:


#? SOLUTION:

#* Python Random module is an in-built module of Python which is used to generate random numbers. These are pseudo-random numbers means these are not truly random. This module can be used to perform random actions such as generating random numbers, print random a value for a list or string, etc.

#* random.randint() method is used to generate random integers between the given range.

#*Syntax >>> randint(start, end)

import random

random_num = random.randint(0,99)

guess_count = 0

while True:

    guess = int(input("Enter a number between 0 to 99: "))

    if guess < random_num:
        print("Enter a higher number..")
        guess_count += 1
    elif guess > random_num:
        print("Enter a lower number..")
        guess_count += 1

    else:
        print("Congrats!")
        guess_count += 1
        break

print(guess_count)
