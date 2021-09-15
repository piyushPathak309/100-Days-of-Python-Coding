# Write a Python program that prints the string s with the character curr_char replaced by the character new_char.
#
# curr_char and new_char are variables that contain strings with a single character.
#
# You may assume that new_char will not be an empty string.
#
# The match must be case-sensitive (do not replace lowercase letters if curr_char is uppercase).
#
# If no match is found, print the initial string

text = input("Enter a text: ")
old = input("Enter Old Character :")
New = input("Enter New Character :")
print(text.replace(old,New))
