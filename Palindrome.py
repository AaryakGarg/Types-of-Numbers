n = int(input("Enter the Number"))
s = 0
d = n
while(n>0):
    r = n%10
    s = s*10+r
    n//=10
if s == d:
    print("The given number is a palindrome")
else:
    print("The given number is not a palindrome")
    
