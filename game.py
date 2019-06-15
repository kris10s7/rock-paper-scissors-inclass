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



computer_choice = random.choice(["rock", "paper", "scissors"])
print("----------")
print("GENERATING...")
print("COMPUTER CHOICE:", computer_choice)
# DETERMINE THE WINNER

# rock beats scissors
# paper beats rock
# scissors beats paper
# same selections is a tie
#
if user_choices == computer_choice:
    print("TIE")
elif user_choices == "rock" and computer_choice == "paper":
    print("PAPER")
elif user_choices == "paper" and computer_choice == "scissors":
    print("SCISSORS")
elif user_choices == "scissors" and computer_choice == "rock":
    print("ROCK")
elif user_choices == "rock" and computer_choice == "scissors":
    print("ROCK")
elif user_choices == "paper" and computer_choice == "rock":
    print("PAPER")
elif user_choices == "scissors" and computer_choice == "paper":
    print("SCISSORS")


# DISPLAY FINAL OUTPUTS / OUTCOMES