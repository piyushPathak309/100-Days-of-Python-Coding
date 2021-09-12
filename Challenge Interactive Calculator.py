# Write a Python program that simulates an interactive calculator with the basic arithmetic operations in Python (addition, subtraction, multiplication, division, integer division, and modulo).
#
# The program must interact with the user by asking for the values and the type of operation that will be performed.
#
# The output should include the values, the operation, and the result (as shown below).
#
# The type of operation will be denoted by an integer.
#
# - 1 for addition
#
# - 2 for subtraction
#
# - 3 for multiplication
#
# - 4 for division
#
# - 5 for integer division
#
# - 6 for modulo
#
# The program should present an initial message to the user describing the types of operations and the integer that has to be entered to select each one of them.
#
# If the values entered by the user are invalid for the operation selected, a descriptive message should be displayed. For example, for a division operation the denominator cannot be 0.
#
# If the user enters an invalid integer to select the operation, print
#
# "Please choose a valid operation"

print("======================== Welcome to the Calculator ==============================")
a= int(input("Enter First Value :"))
b= int(input("Enter Second Value :"))
print("Plz , select any from the below Operation..")
print("For Addition Operation Press 1")
print("For Subtraction Operation Press 2")
print("For Multiplication Operation Press 3")
print("For Division Operation Press 4")
print("For IntegerDivision Operation Press 5")
print("For Modulo Operation Press 6")
op = int(input("Plz Enter Your Command :"))

if op==1:
    c=a+b
    print("The Sum is" ,  c)
elif op==2:
    c=a-b
    print("The Subtraction is" ,  c)
elif op==3:
    c=a*b
    print("The Multiplication is" ,  c)
elif op==4:
    c=a/b
    print("The Division is" ,  c)
elif op==5:
    c=a//b
    print("The IntegerDivision is" ,  c)
elif op==6:
    c=a%b
    print("The Modulo is" ,  c)
else:
    print("Plz Enter Valid Operation")

