# Write a Python program that prints the positive and negative solutions (roots) for a quadratic equation.
#
# If the equation only has one solution, print the solution as the output.
#
# If it has two solutions, print the negative one first and the positive one second on the same line.
#
# If the equation has no real solutions, print "Complex Roots".
#
# You can determine the number of solutions with the discriminant (the result of b^2 - 4ac in the formula below).
#
# - If it's negative, the equation has no real solutions (only complex roots).
#
# - If it's 0, there is only one solution.
#
# - If it's positive, there are two real solutions.
#
# A quadratic equation has this form:
#
#
#
# For example:
#
#
# To solve this equation, we use the quadratic formula:
#
#
# We find the result by replacing the values of a, b, and c in the formula.
import math as m

a = int(input("Enter First Number :"))
b = int(input("Enter Second Number :"))
c = int(input("Enter Third Number :"))
d = (b ** 2 - 4 * a * c)
if (d < 0):
    print("No Real Solution , Complex Roots")
if (d > 0):
    x1 = (-b + (m.sqrt(b ** 2 -4 * a * c))) / (2 * a)
    x2 = (-b - (m.sqrt(b ** 2 -4 * a * c))) / (2 * a)
    print(x1, x2)
if (d == 0):
    p = -b // (2 * a)
    print(p)

