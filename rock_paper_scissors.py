# pylint: disable = missing-module-docstring
import random

USER_WINS = 0
COMPUTER_WINS = 0

options = ["rock", "paper","scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit:  ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        USER_WINS +=1
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        USER_WINS +=1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        USER_WINS +=1

    else:
        print("You lost!")
        COMPUTER_WINS += 1

print("You won", USER_WINS, "times.")
print("The computer won", COMPUTER_WINS, "times.")
print("Goodbye!")
