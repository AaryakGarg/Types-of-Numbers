a = int(input("Enter a number"))
s = 0
d=a
while a>0:
    r =a%10
    s+=r 
    a//=10
if d%s==0:
    print("Niven Number")
else:
    print("Not a Niven Number")
    
    


