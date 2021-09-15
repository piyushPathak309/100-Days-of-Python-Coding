s = input("Enter a String: ")
spl=s.split()
def rev(string):
    string=string[::-1]
    return  string
r=" "
for i in range(len(spl)):
    if i%2==0:
        r=r+rev(spl[i])+" "
    else:
        r=r+spl[i]+" "
print(r)
