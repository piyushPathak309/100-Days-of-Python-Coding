s =input("Enter a String: ")
b=" "
for i in s:
    if i.isalnum() or i==" ":
        b=b+i
print(b)

