# Write a Python program that prints the first and last three characters of the string s as a single string.
#
# If the string has less than six characters, print an empty string (blank output
text = input("Enter a text: ")
s1 =text[0:3]
# print(type(s1))
s2=text[-3:]
print(s1+s2)
