# Write a Python program that prints the corresponding season based on the value of the variable season_num.

# The possible values of season_num are: 1 for Spring, 2 for Summer, 3 for Fall, 4 for Winter.

# If the value of season_num is neither one of these values, print "Please enter a valid number"

Season_num = int(input("Enter Season Number :"))
if Season_num == 1:
    print("Spring")
elif Season_num == 2:
    print("Summer")
elif Season_num == 3:
    print("Fall")
elif Season_num == 4:
    print("Winter")
else:
    print("Enter a valid number")
