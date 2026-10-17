import random

num = random.randint(1, 10)

print("Welcome to Number Guessing Game!")

while True:
    guess = int(input("Guess a number between 1 and 10: "))

    if guess == num:
        print("Congratulations! You guessed it right!")
        break
    elif guess < num:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")