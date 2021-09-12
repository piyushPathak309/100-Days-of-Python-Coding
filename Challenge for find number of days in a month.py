# Write a Python program that prints the number of days in a given month.

# The value of the variable month is the name of the month with the first letter capitalized.

# Do not consider leap years for the number of days in February.

# You can add a customized message. For example: "<month> has: <num_days> days."
Month = input("Enter a Month :")
month = "February"

months_31_days = ("January", "March", "May", "July",
                  "August", "October", "December")

months_30_days = ("April", "June", "September", "November")

if Month in months_31_days:
    print(f"{Month} has: 31 days")
elif Month in months_30_days:
    print(f"{Month} has: 30 days")
else:
    print(f"{Month} has: 28 days")
