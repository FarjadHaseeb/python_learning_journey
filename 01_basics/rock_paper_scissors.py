import random

choices = ["rock", "paper", "scissors"]

while True:
    user = input("Choose rock, paper, scissors or quit: ").lower()
    if user == "quit":
        break
    if user not in choices:
        print("Invalid choice")
        continue

    computer = random.choice(choices)
    print("Computer:", computer)

    if user == computer:
        print("Draw")
    elif (user, computer) in [("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")]:
        print("You win")
    else:
        print("Computer wins")
