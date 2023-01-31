y = "YES"
ans = input("Do you want to find the length of a book name? ").upper()
while ans == y:
    title = input("What is the title of the book? ")
    count = 0
    for char in title:
        count = count + 1
    print("The letters in ", title, "is " ,count, "characters in length")
    ans = input("Would you like to try another book? ").upper()
    if ans == "NO":
        break
    else:
        print("either answer yes or no.")
        ans = input("Would you like to try another book? ").upper()
