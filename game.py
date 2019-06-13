# game.py

print("Rock, Paper, Scissors, Shoot!")

# CAPTURE INPUTS
user_choices = input("Please choose one of the following options: 'rock', 'paper', or 'scissors' (without the quotes):")
print("----------")
print("YOU CHOSE:",user_choices)
# VALIDATE INPUTS

if user_choices in ["rock", "paper", "scissors"]:
    print("VALID")
else:
    print("INVALID SELECTION PLEASE TRY AGAIN")
    exit()

# GENERATE COMPUTER SELECTION

print("GENERATING...")



# DETERMINE THE WINNER

# DISPLAY FINAL OUTPUTS / OUTCOMES