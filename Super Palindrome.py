a = int(input("Enter The Number\n"))
b = a**2
c = str(b)
a = str(a)
d = c[::-1]
e = a[::-1]
if d==c and e==a:
    print("The number is a superpalindrome")
else:
    print("the number is not a superpalindrome")
