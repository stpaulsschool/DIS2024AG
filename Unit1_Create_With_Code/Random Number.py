import random

play = input("would you like to play? y/n: ").upper()
num = random.randint(0, 100)
guesses = 0

while play == "Y":
    print(num)
    guess = int(input("Guess your number"))
    print(guesses)
    if guess == num:
        guesses = guesses + 1
        print(f"You Guessed it in {guesses} tries")
        play == ("would you like to keep playing? y/n: ")
    elif guess < num:
        guesses = guesses + 1
        print("Go Higher")
    elif guess > num:
        guesses = guesses + 1
        print("Go lower")
    else:
        print("enter an interger")


print("thankyou for playing my game.")
