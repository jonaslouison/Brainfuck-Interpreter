import readchar, os

"""print("Reading a Char:")
s= readchar.readkey()
print(s)"""

#bf Command ",": listens for Userinput (single Char from Alphabet) during runntime and saves it into the current cell as integer
array = [0 for i in range (256)]
pointer = 0
asking = True
while asking:
    try:
        #temp = input("Type in only one letter: ")
        #temp = input("A for Left, D for Right: ")
        #print("wasd for Movement: ", end="")
        temp = readchar.readkey()
        os.system('cls||clear')
        if temp.isalpha():
            array[pointer] = ord(temp)
            asking = False
        print(temp)
    except TypeError:
        print ("Wrong Input")
        asking = True