# Write a Python program that prints the character at index i in the string s.
#
# If the index is out of range, the program should print "i is out of range"
#
# If the string is empty, the program should print "Empty String
text = input("Enter a text")
i = int(input("Print Index to see Character "))
if len(text) ==0:
    print("Empty String")
elif i<len(text):
    print(text[i])
else:
    print("Index Out Of Range")
