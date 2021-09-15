# Write a Python program that prints the string s without the characters located at even indices.
#
# If the string is empty or only has one character, print it intact

text = input("Enter a text: ")
i=0
while(i<len(text)):
    if(i%2==0):
        pass
    else:
        print(text[i])
    i=i+1