import sys
class brainfcktest():
    code = ""
    codepointer = 0
    array = [0 for i in range (256)]
    pointer = 0
    allbrackets=[]
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
                j+=1
                self.leftbrackets.append(x)
                v=0
                y=x+1
                while y != len(self.code):
                    if self.code[y]=="]" and v==0:
                        self.rightbrackets.append(y)
                        break
                    elif self.code[y]=="[":
                        v+=1
                    elif self.code[y]=="]" and v != 0:
                        v-=1
                    y+=1
            elif self.code[x] == "]":
                j-=1
            if j < 0:
                print("Failure, Rightbracket at the Codeposition "+ str(x) +" has no matching Leftbracket")
                sys.exit()
            x+=1
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
                self.codepointer = int(self.rightbrackets[self.bracketpointer])
                if len(self.rightbrackets) > self.bracketpointer+1:
                    while self.codepointer > self.rightbrackets[self.bracketpointer+1]:
                        if len(self.rightbrackets) > self.bracketpointer+1:
                            self.bracketpointer+=1
            elif len(self.rightbrackets) > self.bracketpointer+1:
                self.bracketpointer+=1
        # if current cell is not 0 go to the last [
        elif self.code[i] == "]":
            if self.array[self.pointer] != 0:
                self.codepointer = int(self.leftbrackets[self.bracketpointer])-1
                if 0 < self.bracketpointer and len(self.rightbrackets) > self.bracketpointer+1:
                    while self.rightbrackets[self.bracketpointer] < self.rightbrackets[self.bracketpointer+1]:
                        if 0 < self.bracketpointer:
                            self.bracketpointer-=1
            elif len(self.rightbrackets) > self.bracketpointer+1:
                self.bracketpointer+=1
        else:
            print("Unknown Comand at index "+str(i))
            sys.exit()
    def main(self):
        while self.codepointer < len(self.code):
            self.operators(self.codepointer)
            self.codepointer += 1
        print("")
        print ("success")
    #todo: def if __name__ == __main__:

#todo: myocde = input ("Brainf*ck code: ") or doc with .bf
#? Example Code
mycode1 = str("++++++++[>++++++++<-]>+.")# Shorter Code for Letter A (8 Loops)
mycode2 = str("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.") # Letter A in Brainfck
mycode3 = str("++++[>++++++++++++++++<-]>+.") # Letter A with 4 loops
mycode4 = str("+[-[<<[+[--->]-[<<<]]]>>>-]>-.---.>..>.<<<<-.<+.>>>>>.>.<<.<-.") # Hello World!
mycode5 = str("[[]") # returns Error> more '[' than ']'
mycode6 = str(",[.,]") # echos User input
mycode7 = str("][") # returs error > no matching left bracket found
mycode8 = str("++++[>++++[>>++++<<-]>++++[>>++++<<-]<<-]>>>+.") # complicaded A with 3 Loops in this order: [[][]]
mycode9 = str("asdfasffsfsfafasfsadfsa") #returns Error > unknown Code
b = brainfcktest(mycode8)
b.main()
