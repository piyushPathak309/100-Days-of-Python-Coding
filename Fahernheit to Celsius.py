# Write a Python program that converts degrees Fahrenheit to Celsius and prints the result with a descriptive message.
#
# The user should enter the degrees Fahrenheit.
#
# To convert degrees Fahrenheit to Celsius, we use this formula:
#
# <degrees_celsius> = (<degrees_fahrenheit> - 32) * 5/9
#
# The message should have this format:
#
# "<degrees> Fahrenheit = <degrees> Celsius"
#
F = float(input("Enter Temprature in Fahrenheit :"))
C = ((F-32)*5)/9
Temp=round(C,2)
print("The Celsius Temprature is as " , Temp)
