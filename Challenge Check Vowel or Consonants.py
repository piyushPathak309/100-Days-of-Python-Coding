# Write a Python program that prints a descriptive message indicating if each character in a string is a vowel or a consonant.
# For example: "<char> is a <consonant | vowel>"

# If the character is a special character, number, or symbol, print "<char> is not a letter".

# If the string is empty, print "Empty String".
# Expected Output:
# If the string is:

# "Score: 36"

# The expected output would be:

# s is a consonant
# c is a consonant
# o is a vowel
# r is a consonant
# e is a vowel
#: is not a letter
# is not a letter
# 3 is not a letter
# 6 is not a letter

Text = input("Enter a Text :")
if not Text:
    print("Empty String")
else:
    for char in Text.lower():
        if char in ("a", "e", "i", "o", "u"):
            print(f"{char} is a vowel")
        elif not char.isalpha():
            print(f"{char} is not a letter")

        else:
            print(f"{char} is a consonant")

