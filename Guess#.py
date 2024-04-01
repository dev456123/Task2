import random
import time

def intro():
    print("May I ask you for your name?")
    name = input()  # asks for the name
    print(name + ", we are going to play a game. I am thinking of a number between 1 and 200.")
    time.sleep(0.5)
    print("Go ahead. Guess!")
    return name  # return the name entered by the user

def pick(name):  # pass the 'name' variable as an argument
    number = random.randint(1, 200)  # pick the number between 1 and 200
    guesses_taken = 0
    while guesses_taken < 6:  # if the number of guesses is less than 6
        try:  # check if a number was entered
            guess = int(input("Guess: "))  # inserts the place to enter guess
            if 1 <= guess <= 200:  # if they are in range
                guesses_taken += 1  # adds one guess each time the player is wrong
                if guess < number:
                    print("The guess is too low.")
                elif guess > number:
                    print("The guess is too high.")
                else:
                    print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
                    return
                print("Try Again!")
            else:  # if they aren't in the range
                print("Silly Goose! That number isn't in the range!")
                print("Please enter a number between 1 and 200.")
        except ValueError:  # if a non-numeric value was entered
            print("I don't think that's a number. Sorry.")

    print(f"Sorry, {name}. The number I was thinking of was {number}.")

play_again = "yes"
while play_again.lower() in ["yes", "y"]:
    name = intro()  # assign the returned name from intro() to the 'name' variable
    pick(name)  # pass the 'name' variable to the pick() function
    print("Do you want to play again? (yes/no)")
    play_again = input()

print("Thanks for playing!")
