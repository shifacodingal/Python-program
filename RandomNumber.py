import random

num = random.randint(1, 10)
name = input("Hey ! Let's be friends 😀. \nMay I know your name : ")
print("Welcome to Number Guessing Game!")

while True:
    guess = int(input("Guess a number between 1 and 10: "))

    if guess == num:
        print("🎉Congratulations ",name,"! You guessed it right!")
        break
    elif guess < num:
        print("Too low! please try again ",name,".")
    else:
        print("Too high! please try again ",name,".")