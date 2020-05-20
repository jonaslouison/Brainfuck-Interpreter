#!/usr/bin/env python
import sys
class brainfck():
    code = ""
    codepointer = 0
    array = [0 for i in range (256)]
    pointer = 0
    def __init__(self, mycode):
        self.code = mycode
        self.testbracktes()
    def testbracktes(self):
        #detects errors like those '][', '[]]'
        j=0 
        x=0 
        while x != len(self.code):
            if self.code[x] == "[":
                j+=1
            elif self.code[x] == "]":
                j-=1
            if j < 0:
                print("Failure, Rightbracket at the Codeposition "+ str(x) +" has no matching Leftbracket")
                sys.exit()
            x+=1
        if j != 0:
            print("Failure, Amount of '[' should be the same as ']'")
            sys.exit()
    def operators(self, i):
        if self.code[i] == ">":
            # moves Pointer by 1
            if self.pointer == 255:
                self.pointer = 0
            else:
                self.pointer += 1
        elif self.code[i] == "<":
            # moves Pointer by -1
            if self.pointer == 0:
                self.pointer = 255
            else:
                self.pointer -= 1
        elif self.code[i] == "+":
            # changes value in list/array by 1
            if self.array[self.pointer] == 255:
                self.array[self.pointer] = 0
            else:
                self.array[self.pointer] += 1
        elif self.code[i] == "-":
            # changes value in list/array by -1
            if self.array[self.pointer] == 0:
                self.array[self.pointer] = 255
            else:
                self.array[self.pointer] -= 1
        elif self.code[i] == ".":
            # prints the Char of current cell 
            print(chr(self.array[self.pointer]),end="")
        elif self.code[i] == ",":
            # listens for Userinput (single Char from Alphabet) during runntime and saves it into the current cell as integer
            print()
            asking = True
            while asking:
                try:
                    #temp = input("Type in only one letter: ")
                    temp = input("A for Left, D for Right: ")
                    if temp.isalpha():
                        self.array[self.pointer] = ord(temp)
                        asking = False
                except TypeError:
                    print ("Wrong Input")
                    asking = True
        elif self.code[i] == "[":
            # if current cell is 0 go to code behind next ]
            if self.array[self.pointer] == 0:
                x = 1 
                while x != 0 and self.codepointer < len(self.code)-1:
                    self.codepointer += 1
                    if self.code[self.codepointer] == "[":
                        x += 1
                    elif self.code[self.codepointer] == "]":
                        x -= 1
        elif self.code[i] == "]":
            # if current cell is not 0 go to the last [
            if self.array[self.pointer] != 0:
                y = -1
                while y != 0 and self.codepointer > 1:
                    self.codepointer -= 1
                    if self.code[self.codepointer] == "[":
                        y += 1
                    elif self.code[self.codepointer] == "]":
                        y -= 1
        else:
            # detects Unknown Command and breaks the Program
            print("Unknown Comand at index "+str(i))
            sys.exit()
    def main(self):
        while self.codepointer < len(self.code):
            self.operators(self.codepointer)
            self.codepointer += 1
        print ("\nSuccess")
    #todo: def if __name__ == __main__:

#todo: myocde = input ("Brainf*ck code: ") or doc with .bf
#? Example Code
mycode1 = str("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.") # Letter A in Brainfck
mycode2 = str("++++++++[>++++++++<-]>+.")# Shorter Code for Letter A (8 Loops)
mycode3 = str("++++[>++++++++++++++++<-]>+.") # Letter A with 4 loops
mycode4 = str("++++[>++++[>>++++<<-]>++++[>>++++<<-]<<-]>>>+.") # complicaded A in this order: [[][]]

mycode5 = str("[[]") # returns Error > more '[' than ']'
mycode6 = str("[]][") # returs Error > no matching left bracket found
mycode7 = str("asdfasffsfsfafasfsadfsa") #returns Error > unknown Code

mycode8 = str("+[-[<<[+[--->]-[<<<]]]>>>-]>-.---.>..>.<<<<-.<+.>>>>>.>.<<.<-.") # hello world
mycode9 = str("+[-->-[>>+>-----<<]<--<---]>-.>>>+.>>..+++[.>]<<<<.+++.------.<<-.>>>>+.") # Hello World!
mycode10 = str(",[.,]") # echos User input
mycode11 = str(",+.") # echos next Char from Userinput
mycode12 = str("++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>----.>++++++++++++++.-----------------.++++++++.+++++.--------.---.++++++++.<<++.>>--.++++++++++.<<.>-.>++++.----.----.--.--------.<<+.")
mycode13 = str("+++++[>[>],[<]>-]>.>.>.>.>.") # Returns the 5 digit name which is typed in Letter for Letter by User

#? Little Game > Move 0 with A to Left and D to Rigth, Ascii: "."= 46, "0"= 48, "new Line"=10, "A" == 65, "D"= Any other Key
mycode14 = str("<++++++++[[>]>++++++++[<++++++>-]+<--[<]>-]>++.>-.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.") # Sets up "0NUL.SOH.SOH.SOH.SOH.SOH.SOH.SOH" at Array[0]
mycode15 = str("<++++++++[[>]>++++++++[<++++++>-]+<--[<]>-]>++>-<<-.>.>.>.>.") # Last "-" sets Playtime to 255 at Array[255], use "," instead if you want to configure it yourself
mycode16 = str("<++++++++[[>]>++++++++[<++++++>-]+<--[<]>-]>++>-<<-[<,.>-.]") # Set User Input(UI) in Array[254]
mycode17 = str("<++++++++[[>]>++++++++[<++++++>-]+<--[<]>-]>++>-<<-[<,<[-]<[-]++++++++[>++++++++<-]>+.>.>.>[.>>]<<[<<]>>>-]") # Sets "A" for Left Movement at Array[253]
# Controlcells begin at Array[253] and look like this "A UI 255 0 NUL . SOH"... now
#Detects that A is not pressed
mycode18 = str("<++++++++[[>]>++++++++[<++++++>-]+<--[<]>-]>++>-<<-[<,<[-]<[-]++++++++[>++++++++<-]>+[>-<-]+>[<->[-]>>>[>>]<-->+>++>-<[<]]<[->>>>[>>]+<--<-<++[<]<]>>>[.>>]<<[<<]>-]")
#Set 0 to the left verry left if it passed the rigth boundarry
mycode19 = str("<++++++++[[>]>++++++++[<++++++>-]+<--[<]>-]>++>-<<-[<,<[-]<[-]++++++++[>++++++++<-]>+[>-<-]+>[<->[-]>>>[>>]<-->+>++>-<[<]]<[->>>>[>>]+<--<-<++[<]<]>>>[.>>]<<[<<]>-]")

mycode20 = str("-[.-]") # Return the Asciitable backwards, change "-" with "+" for returning it forwards

b = brainfck(mycode18)
b.main()
