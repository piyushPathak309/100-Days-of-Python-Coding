# Write a Python program that prints the digits of a number in reverse order on the same line.
#
# If the number only has one digit, print this digit.
x = int(input("Enter a Number :"))
rev = 0
while x>0:
    r=x%10
    rev=rev*10+r
    x=x//10
print(rev)