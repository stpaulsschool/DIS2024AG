#welcome text
print("Welcome to the company name analyser")
i = 0
cn = " "
while cn != "q":
    cn = input("Please enter company name or enter 'q' if you would like to quit.")
    if cn == "q":
        break
    elif cn != "q":
        cnlist = cn.split()
        print(cnlist)
        i += 1
    length = len(cnlist)
    for length in length:
        i = i+1
if i <= 2:
    print("your book name will sell well")
elif i > 2:
    print("shorten your name to get better sales")


    #elif length >= 2:
       # print("your book name will sell well")
   # else:
      #  print("shorten your name to get better sales")

