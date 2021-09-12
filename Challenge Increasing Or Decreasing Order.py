# Write a Python program that determines if three numbers (a, b, and c) are in increasing order, decreasing order, or none.

# If a > b > c, print "Decreasing Order".

# If a < b < c, print "Increasing Order".

# Else, print "None".
x = int(input("Enter First Number :"))
y = int(input("Enter Second Number :"))
z = int(input("Enter Third Number :"))
if (x > y > z):
    print("decreasing Order")
elif (x < y < z):
    print(" Increasing  Order")
else:
    print("None")
