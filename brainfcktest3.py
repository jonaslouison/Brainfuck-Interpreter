import sys
class brainfcktest():
    code = ""
    codepointer = 0
    array = [0 for i in range (256)]
    pointer = 0 # this is the arraypointer
    leftbrackets = []
    rightbrackets = []
    bracketpointer = 0
    def __init__(self, mycode):
        self.code = mycode
        self.fillBracketArrays()
    def fillBracketArrays(self):
        j=0 #detects errors like those '][', '[]]'
        x=0 
        while x != len(self.code):
            if self.code[x] == "[":
                self.leftbrackets.append(x)
                j+=1
            elif self.code[x] == "]":
                self.rightbrackets.insert(0, x)
                j-=1
            x+=1
            if j < 0:
                print("Failure, Rigthbracket at the Codeposition "+ str(x) +" has no matching Leftbracket")
                sys.exit()
        #j != 0:  #would also be possible
        if len(self.leftbrackets)!=len(self.rightbrackets):
            print("Failure, Amount of '[' should be the same as ']'")
            sys.exit()
    def operators(self, i):
        # moves Pointer (+1 or -1)
        if self.code[i] == ">":
            if self.pointer == 255:
                self.pointer = 0
            else:
                self.pointer += 1
        elif self.code[i] == "<":
            if self.pointer == 0:
                self.pointer = 255
            else:
                self.pointer -= 1
        # changes value in list/array (+1 or -1)
        elif self.code[i] == "+":
            if self.array[self.pointer] == 255:
                self.array[self.pointer] = 0
            else:
                self.array[self.pointer] += 1
        elif self.code[i] == "-":
            if self.array[self.pointer] == 0:
                self.array[self.pointer] = 255
            else:
                self.array[self.pointer] -= 1
        # writes the Char of current cell in the answer which is printed later
        elif self.code[i] == ".":
            print(chr(self.array[self.pointer]),end="")
        # listens for Userinput (single Char from Alphabet) during runntime and saves it into the current cell as integer
        elif self.code[i] == ",":
            print()
            asking = True
            while asking:
                try:
                    temp = input("Type in only one letter: ")
                    if temp.isalpha():
                        self.array[self.pointer] = ord(temp)
                        asking = False
                except TypeError:
                    print ("Wrong Input")
                    asking = True
        # if current cell is 0 go to code behind next ]
        elif self.code[i] == "[":
            if self.array[self.pointer] == 0:
                while self.code[self.codepointer] != "]":
                    self.codepointer += 1
        # if current cell is not 0 go to the last [
        elif self.code[i] == "]":
            if self.array[self.pointer] != 0:
                while self.code[self.codepointer] != "[":
                    self.codepointer -= 1
    def main(self):
        while self.codepointer != len(self.code):
            self.operators(self.codepointer)
            self.codepointer += 1
        print("")
        print ("success")
    #todo: def if __name__ == __main__:

#todo: myocde = input ("Brainf*ck code: ")
#? Example Code
mycode1 = str("++++++++[>++++++++<-]>+.")# Shorter Code for Letter A (8 Loops)
mycode2 = str("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.") # Letter A in Brainfck
mycode3 = str("++++[>++++++++++++++++<-]>+.") # Letter A with 4 loops
mycode4 = str("+[-[<<[+[--->]-[<<<]]]>>>-]>-.---.>..>.<<<<-.<+.>>>>>.>.<<.<-.") # Hello World!
mycode5 = str("[[]") # returns Error> more '[' than ']'
mycode6 = str(",[.,]") # echos User input
mycode7 = str("][") # returs error > no matching left bracket found
mycode8 = str("+[>+<-]>.")
b = brainfcktest(mycode4)
b.main()
