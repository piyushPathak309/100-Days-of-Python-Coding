#Write a Python program that prints the maximum of three integers (a, b, c).
a = int(input("Enter First Number :"))
b = int(input("Enter Second Number :"))
c = int(input("Enter Third Number :"))
if (a > b & a > c):
    print(a, " is", "Greatest")

if (b > a & b > c):
    print(b, " is", "Greatest")

if (c > a & c > b):
    print(c, " is", "Greatest")

# Alternate using Max function
#print(max(a,b,c))
