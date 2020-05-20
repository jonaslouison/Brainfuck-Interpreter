class arraytest():
    #* Varibles
    array = []
    codepointer = 0
    
    #* fills array
    def newArray(self):
        for x in range (20):
            self.array.insert(x, x*10)
    
    #* prints Array
    def main(self):
        self.newArray()
        """for self.codepointer in range(len(self.array)):
            print (self.array[self.codepointer])
            self.codepointer += 3"""
        while self.codepointer < len(self.array):
            print (self.array[self.codepointer])
            self.codepointer += 3

test= arraytest()
test.main()
