def frnd(a):
    f = 1
    while a>0:
        f*=10
        a//=10
    return f
n = int(input("enter the number"))
n2 = n**2
n3 = frnd(n)
k = n2%n3
k2 = n2//n3
if n == (k+k2):
    print("Kaprekar Number")
else:
    print("Not Kaprekar Number")
    
#kaprekar number eg - a = 45, (45**2) = 2025 and if we split 2025
# 20 + 25 = 45 , so 45 is a kaprekar number
