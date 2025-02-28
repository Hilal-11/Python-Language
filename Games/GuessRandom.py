
import random

def guess(n) :
    random_number = random.randint(1 , n)
    guess = 0
    while (guess != random_number) :
        guess = int(input(f"Guess the random between 1 to {n} :-"))
        if(guess > random_number) :
            print("sorry guess again, guess is too high")
        elif (guess < random_number) :
            print("sorry guess again, guess is too low")
            
    print("hey 😃 congratulation you guess the correct number")
        

guess(10)