import random 
import time

number = random.randint(1,100)
print ("The number is chosen please guess")

def intro ():
    print ("May I know your name?")
    global name 
    name = input ()
    
    print ( name +"Welcome to the game. Guess the random number from 1 to 100 ")
    if number%2 == 0:
        x = "even"
    else:
        x = "odd"
    print ("Hint: The number is ", x, "number")
    time.sleep (.5)
    print ("Go ahead! and guess again")

def pick ():
        Guess_Taken = 0
        while Guess_Taken < 6:
            time.sleep (.25)
            enter = input("Guess : ")
            try:
                guess = int(enter)
                print(guess)
                print(number)
                if guess<= 100 and guess>=1:
                    Guess_Taken = Guess_Taken+1 
                    if Guess_Taken < 6:
                        if guess < number:
                            print ("The number is too low")
                        if guess > number:
                            print ("Guess is too high")
                        if guess != number:
                            print ("Try Again")
                        if guess == number:
                            break
                if guess > 100 or guess < 1:
                    print ("Silly Goose!. The Number is not even in the range")
                    time.sleep (.25)
                    print ("Enter a number between the range of 1 to 100")
            except:
                print ("Enter a number value only")
        if guess == number:
            Guess_Taken = str(Guess_Taken)
            print ("Good job!!!", name, "You guessed my number under", Guess_Taken, "Guesses")
        if guess != number:
            print ("OOPS! You guessed it incorrectly", name, "The number was : ", +str (number))
playing = "yes"
while playing == "yes":
    intro ()
    pick ()
    print ("Do you want to continue")
    playing = input()





