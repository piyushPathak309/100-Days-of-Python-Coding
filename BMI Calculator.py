# Write a Python program that calculates body mass index.
#
# The formula to calculate body mass index is BMI = kg/m2 where kg is a person’s weight in kilograms and m2 is their height in meters squared.
#
# The user should be able to enter his or her height in centimeters and weight in kilograms.
#
# You may assume that the height and weight entered will be positive integers.
#
# The program must print a message with the value of the Body Mass Index (BMI) rounded to two decimals and the category:
#
# Underweight = less than 18.5
#
# Normal = from 18.5 to 24.9
#
# Overweight = from 25 to 29.9
#
# Obesity = 30 or greater
w = float(input("Enter Weight: "))
h = float(input("Enter Height: "))
Bmi = w / (h * h)
if Bmi < 18.5:
    print("Underweight")
elif 18.5 > Bmi < 24.9:
    print("Normal")
elif 25 > Bmi < 29.9:
    print("Overweight")
elif Bmi > 30:
    print("Obesity")
else:
    print("Not Calculated")