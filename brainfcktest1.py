class brainfck():
    #* initialisation of variables
    #? points to current cell in array
    pointer = 0
    #? list for saving integers during runntime
    array =[256]
    #* Get Brainf*ck code from User via comand line
    code = input("Type in your Brainf*ck Code here:   ")
    
    #* define operators, the parameter i is the location where operator was used in the users code
    def operators(self, i):
        # moves Pointer
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
        # changes value in list/array
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
        # writes the value of current cell in the answer which is printed later
        elif self.code[i] == ".":
            self.answer.append(self.array[self.pointer])
        # listens for Userinput during runntime and saves it into the current cell
        elif self.code[i] == ",":
            asking = True
            while asking:
                temp = str(input("Type in a letter: "))
                if temp.isalpha():
                    self.array[self.pointer] = temp
                    asking = False
        elif self.code[i] == "[":
            pass
        elif self.code[i] == "]":
            pass
    
    def main(self):
        for x in len(self.code):
            operators(self, x)