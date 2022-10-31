
#! ROCK-PAPER-SCISSORS

#? SOLUTION:

print("Let's play a game...")

a = input("Do you wanna play Rock-Paper-Scissors? (Yes or No): ").lower()

import random

pc_list = ["rock", "paper", "scissors"]

while a == "yes":
    pc = pc_list[random.randint(0,2)]
    you = input("Choose one >> rock paper or scissors: ").lower()

    if (pc == "rock" and you == "scissors") or (pc == "paper" and you == "rock") or (pc == "scissors" and you == "paper"):
        s = "PC Win!"

    elif (pc == "rock" and you == "paper" or (pc == "paper" and you == "scissors") or (pc == "scissors" and you == "rock")):
        s= "You Win!"

    elif (pc == "rock" and you == "rock" or (pc == "paper" and you == "paper") or (pc == "scissors" and you == "scissors")):
        s = "Draw Game"
    else:
        s = "You entered wrong"

    print(s)

    a = input("Do you wanna play Rock-Paper-Scissors? (yes or no)").lower()

print("Game over..")