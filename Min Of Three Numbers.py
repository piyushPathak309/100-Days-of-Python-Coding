#Write a Python program that prints the minimum of three integers (a, b, c).
a = int(input("Enter First Number :"))
b = int(input("Enter Second Number :"))
c = int(input("Enter Third Number :"))
if (a < b & a < c):
    print(a, " is", "Smallest")

if (b < a & b < c):
    print(b, " is", "Smallest")

if (c < a & c < b):
    print(c, " is", "Smallest")

# Alternate using Min function
# print(min(a,b,c))