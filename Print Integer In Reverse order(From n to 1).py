# Write a Python program that prints the integers between a given number n and 1 (in descending order, both inclusive).
#
# The value of n should be entered by the user and you may assume that it is an integer greater than or equal to 1.
#
# Use a loop to print each number on a separate line.
#
# 🔹 Expected Output:
# If n is equal to 6:
#
# 6
# 5
# 4
# 3
# 2
# 1
# If n is equal to 10:
#
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
n = int(input("Enter a Number :"))
for i in range(n, 0, -1):
    print(i)


