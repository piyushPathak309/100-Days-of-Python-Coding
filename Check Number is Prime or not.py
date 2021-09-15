# Write a Python program that checks if a number is prime or not.
#
# If the number is prime, it should print "Prime".
#
# If the number is not prime, it should print "Not prime".
#
# A prime number is only divisible by 1 and by itself. It is not the product of two smaller natural numbers.
n = int(input("Enter a Number :"))
count=0
for i in range(1,n+1):
    if(n%i==0):
        count=count+1
if(count==2):
    print(" Prime Number")
else:
    print("Not a Prime Number")