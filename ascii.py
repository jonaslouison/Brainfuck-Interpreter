# Add each character, and it's ordinal, of user's text input, to two lists
#* from https://en.wikibooks.org/wiki/Python_Programming/Text
#* chr() and ord(): https://www.askpython.com/python/built-in-methods/python-chr-and-ord-methods
s = input("Enter value: ")  # this line requires Python 3.x, use raw_input() instead of input() in Python 2.x

l1=[c for c in s]   # in Python, a string is just a sequence, so we can iterate over it!
l2=[ord(c) for c in s]

print(l1)
print(l2)





#! Variant:
"""# Add each character, and it's ordinal, of user's text input, to two lists
s = input("Enter value: ")  # this line requires Python 3.x, use raw_input() instead of input() in Python 2.x
l1 = [] 
l2 = []
for c in s:   # in Python, a string is just a sequence, so we can iterate over it!
    l1.append(c) 
    l2.append(ord(c))
print(l1)
print(l2)"""