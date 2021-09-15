# Write a Python program that prints a string reversed using a loop.
# All the characters must be on the same line in reverse order.
x = input("Enter a String :")
for i in range(len(x)-1, -1, -1):
    print(x[i],end=" ")
