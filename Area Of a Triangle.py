# Write a Python program that computes the area of a triangle from its base and height.
#
# The program should print the area of the triangle rounded to two decimal places (if necessary).
#
# The values of base and height should be entered by the user.
#
# The area of a triangle is found with this formula: (base*height)/2
#
# If either one of the values is invalid, the program should print
#
# "Please enter valid values for base and height".
#
#
b = float(input("Enter Base of a Triangle :"))
h = float(input("Enter Height of a Triangle :"))
Area = (b*h)//2
print("Area of a Triangle is as", Area)