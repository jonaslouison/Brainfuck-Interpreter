# Letter A in Brainfck: +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.
class brainfcktest():
    code = ""
    array = [int(0)]*256
    pointer = 0
    answer = []
    codepointer = 0
    def __init__(self, mycode):
        self.code = mycode
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
            self.answer.append(chr(self.array[self.pointer]))
        # listens for Userinput (single Char from Alphabet) during runntime and saves it into the current cell as integer
        elif self.code[i] == ",":
            asking = True
            while asking:
                temp = input("Type in a letter: ")
                if temp.isalpha():
                    self.array[self.pointer] = ord(temp)
                    asking = False
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
        for self.codepointer in range(len(self.code)):
            self.operators(self.codepointer)
        for j in range(len(self.answer)):
            print(self.answer[j], end="")
        #print()
        print ("success")
    #todo: def if __name__ == __main__:

b = brainfcktest(str("++++++++[>++++++++<-]>+."))
b.main()
