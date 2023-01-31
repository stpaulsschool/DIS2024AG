import time
print ("Welcome to amazon company name shortener. Enter you company name (Min 3 words) and we will show you a shortened name.")
time.sleep(1)
ans = "Y"
while ans == "Y":
    string = input("Enter your company name here: ")
    def shorten_string(string):
        words = string.split()
        if len(words) <= 2:
            return string
        else:
            return ' '.join(words[:2])
    time.sleep(1)
    print("The origional name was:", string)
    time.sleep(1)
    print("The shortened name is:", shorten_string(string))
    if ans =="N":
        break
    if ans == "Y":
        time.sleep(2)
        ans = input("Type 'y' to use this system again or anything else to end the code: ").upper()
time.sleep(2)
print("Thankyou for using the amazon company name shortening system (ACNSS)")