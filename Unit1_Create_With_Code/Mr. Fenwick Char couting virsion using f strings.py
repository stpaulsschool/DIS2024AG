question = "What is the title of the book? "
print("Welcome to my Book Title counter.")
print("Enter the title of a book and I will count the characters.")
title = input(question)
count = 0
runagain = "y"
while runagain == "y":
#for char in title:
#    count = count + 1
#print(count)
    print(f"'{title}' is {len(title)} characters in length.")
    runagain = input("Do you want to try another book? ")

print("Thanks for trying my program. See you next time.")