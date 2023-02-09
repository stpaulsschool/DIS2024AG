import random
# first attempt
# parts taken from here into final code below.

"""import random

play = input("would you like to play? y/n: ").upper()
num = random.randint(0, 100)
guesses = 0
while play == "Y":
    while guesses < 6:
        print(num)
        play == ("would you like to keep playing? y/n: ")
        guess = int(input("Guess your number, (0-100)"))
        if guess == num:
            guesses = guesses + 1
            print(f"You Guessed it in {guesses} tries")
        break
        elif guess < num:
            guesses = guesses + 1
            print("Go Higher")
        elif guess > num:
            guesses = guesses + 1
            print("Go lower")




print("thankyou for playing my game.")"""

'''difi = int(input("enter a number of 1 - 3 please: "))
        if difi == 1:
             guess limit = 7
            guesses = 0
        elif difi == 2:
            guess limit = 6
            guesses = 0
        elif difi == 3:
            guess limit = 5
            guesses = 0'''


play = input("Would you like to play? y/n: ").upper()
guesses = 0
while play == "Y":
    num = random.randint(0, 100)
    # selecting difficulty with difi as variable
    difi = int(input("what difficulty would you like? 1, 2 or 3.  (3 being the hardest): "))
    if difi == 1:
        guess_limit = 7
        guesses = 0
    elif difi == 2:
        guess_limit = 6
        guesses = 0
    elif difi == 3:
        guess_limit = 5
        guesses = 0
    # a way to help with human error
    else:
        guess_limit = 0
    while guesses < guess_limit:
        print(f"You have {guess_limit - guesses} tries left")
        # printing the amount of tries left every time the user is about to guess
        guess = int(input("Guess your number, (0-100)"))
# content copied from above.
        if guess == num:
            guesses = guesses + 1
            print(f"You Guessed it in {guesses} tries")
            break
        elif guess < num:
            guesses = guesses + 1
            print("Go Higher")
        elif guess > num:
            guesses = guesses + 1
            print("Go lower")
    if guesses >= guess_limit:
        print("Oh no, you hit the guess limit! you lost :(")
    play = input("Would you like to play again? y/n: ").upper()
print("Thankyou for playing my game.")
