n = int(input("enter the number"))
d = n
s=0
while n>0:
    r = n%10
    f = 1
    for i in range(1,r+1,1):
        f*=i
    s+=f
    n//=10
if s==d:
    print("number is a special number")
else:
    print("number is not a special number")

        
