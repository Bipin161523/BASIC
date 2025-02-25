a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
if a>b and a>c:
    print("first number is greatest",a)
elif b>a and b>c:
    print("second number is greatest",b)
else: 
    print("third number is greatest",c)