# Write a Python program that prints "Equal" if three numbers a, b, and c are equal.

# If at least one number if different, the program should print "Not Equal".
x = int(input("Enter First Number :"))
y = int(input("Enter Second Number :"))
z = int(input("Enter Third Number :"))
if (x == y == z):
    print("Equal All")
else:
    print("Not Equal ,Atleast One Different")
