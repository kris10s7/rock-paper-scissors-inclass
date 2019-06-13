# game.py

import random

print("Rock, Paper, Scissors, Shoot!")

# CAPTURE INPUTS
user_choices = input("Please choose one of the following options: 'rock', 'paper', or 'scissors' (without the quotes):")
print("----------")
print("YOU CHOSE:",user_choices)
# VALIDATE INPUTS

if user_choices in ["rock", "paper", "scissors"]:
    pass
else:
    print("INVALID SELECTION PLEASE TRY AGAIN")
    exit()

# GENERATE COMPUTER SELECTION

print("GENERATING...")

computer_choice = random.choice(["rock", "paper", "scissors"])
print("----------")
print("COMPUTER CHOICE:", computer_choice)
# DETERMINE THE WINNER

# DISPLAY FINAL OUTPUTS / OUTCOMES