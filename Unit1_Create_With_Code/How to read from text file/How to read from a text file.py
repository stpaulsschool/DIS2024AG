with open("mytextfile.txt", "r") as file: #open file from read - "r" access
    print(file.read()) # read file

mylist = ["a", "b", "c"]

for item in mylist: #for item in list
    with open("mytextfile.txt", "a") as file: # open the file with access
        file.write(item) # write each item in list
        file.write("\n") # write a new line

with open("mytextfile.txt", "r") as file: #open file from read - "r" access
    print(file.read()) # read file

for item in mylist: #for item in list
    with open("mytextfile.txt", "w") as file: # open the file with access
        file.write(" ") # write each item in list
        file.write("\n") # write a new line