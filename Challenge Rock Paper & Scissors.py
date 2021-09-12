# Write a Python program that simulates the "Rock, Paper, Scissors" game.
#
# The game should ask the user to enter an option (either "Rock", "Paper", or "Scissors").
#
# The player should play against the computer, which will select a random option.
#
# The computer's selection will be compared against the player's selection to determine who wins.
#
# A descriptive message should be displayed indicating if the player won, lost, or if the game ended in a tie.
#
# To learn more about this game before starting to solve this challenge, I recommend reading this resource.
#
# Basic Game Rules:
#
# Paper beats Rock
#
# Rock beats Scissors
#
# Scissors beat Paper.
#
# 🔹 Expected Output:
# Sample Game 1:
#
# ====== Welcome to the game ======
# Please enter Rock, Paper, or Scissors below:
# Rock
# It's a tie! Try again.
import random

options = ("rock", "paper", "scissors")

computer = options[random.randint(0, 2)]

print("====== Welcome to the game ======")
player = input("Please enter Rock, Paper, or Scissors below:\n")

if player.lower() == computer:
    print("It's a tie! Try again.")
elif player.lower() == "rock":
    if computer == "paper":
        print("You lose! Your opponent chose 'Paper'")
    else:
        print("You win! Your opponent chose 'Scissors'")
elif player.lower() == "paper":
    if computer == "scissors":
        print("You lose! Your opponent chose 'Scissors'")
    else:
        print("You win! Your opponent chose 'Rock'")
elif player.lower() == "scissors":
    if computer == "rock":
        print("You lose! Your opponent chose 'Rock'")
    else:
        print("You win! Your opponent chose 'Paper'")
else:
    print("Please enter a valid option.")
