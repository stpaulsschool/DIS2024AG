import random
play = input("Would you like to play? Y/N: ").upper()
while play == "Y":
    num = random.randint(0, 100)
    print(num)
    # selecting difficulty with difi as variable
    name = input("What is your name?: ")
    guesses = None
    guess_limit = None
    while not guesses:
        difi = int(input("what difficulty would you like? 1, 2 or 3.  (3 being the hardest): "))
        match difi:
            case 1:
                guess_limit = 7
                guesses = 1
            case 2:
                guess_limit = 6
                guesses = 1
            case 3:
                guess_limit = 5
                guesses = 1
    guesses = guesses - 1
    while guesses < guess_limit:
        print(f"You have {guess_limit - guesses} tries left")
        # printing the amount of tries left every time the user is about to guess
        guess = int(input("Guess your number, (0-100): "))
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
        print(f"Noo, you hit the guess limit! you lost :( The number was {num}. You were only {abs(num - guess)} off!")
    with open("mytextfile.txt", "a") as file:# open the file with access
        file.write(f"{name} guessed the number in {guesses} tries. On dificulty level {difi}!")
        file.write("\n")
    print("-------scores-------")
    with open("mytextfile.txt", "r") as file:  # open file from read - "r" access
        print(file.read())
    print("-----Scores-end-------")
    play = input("Would you like to play again? Y/N: ").upper()
print("Thankyou for playing my game.")
