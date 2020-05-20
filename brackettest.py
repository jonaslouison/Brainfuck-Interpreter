import sys
code =str("[[[]]]")
print (len(code))
codepointer=0
array=[]
leftbrackets=[]
rightbrackets=[]
def bracketfiller():
    j=0 #detects errors like those '][', '[]]'
    x=0 
    while x != len(code):
        if code[x] == "[":
            j+=1
            leftbrackets.append(x)
            v=0
            y=x+1
            while y != len(code):
                if code[y]=="]" and v==0:
                    rightbrackets.append(y)
                    break
                elif code[y]=="[":
                    v+=1
                elif code[y]=="]" and v != 0:
                    v-=1
                y+=1
        """elif self.code[x] == "]":
            j-=1
        if j < 0:
            print("Failure, Rigthbracket at the Codeposition "+ str(x) +" has no matching Leftbracket")
            sys.exit()"""
        x+=1
    #j != 0:  #would also be possible
    if len(leftbrackets)!=len(rightbrackets):
        print("Failure, Amount of '[' should be the same as ']'")
        sys.exit()

bracketfiller()
print(leftbrackets)
print(rightbrackets)
