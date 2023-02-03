print("Welcome to the company name analyser")
#count = 0
cn = " "
while cn != "q":
    count = 0
    cn = input("Please enter company name or enter 'q' if you would like to quit: ")
    if cn == "q":
        break
    elif cn != "q":
        cnlist = cn.split()
        #print(cnlist)
    for item in cnlist:
        #print(item)
        count = count + 1
    if count <= 2:
        print(f"Your company name is '{cn}', it is {count} words in length. ")
    elif count > 2:
        print(f"Your name is {count} words in length. Shorten your name to get better sales. ")
    #print(count)
print("Thanks for using my program.")