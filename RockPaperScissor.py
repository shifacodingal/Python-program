import random

choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)

print("Welcome to Rock Paper Scissors!")

player = input("Enter rock, paper, or scissors: ").lower()

print("Computer chose:", computer)

if player == computer:
    print("It's a Draw!")
elif player == "rock" and computer == "scissors":
    print("You Win!")
elif player == "paper" and computer == "rock":
    print("You Win!")
elif player == "scissors" and computer == "paper":
    print("You Win!")
elif player in choices:
    print("Computer Wins!")
else:
    print("Invalid Choice!")