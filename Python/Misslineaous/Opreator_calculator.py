a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = input("Enter opreator:")
if(c=="+"):
    print(a+b)
elif(c=="-"):
    print(a-b)
elif(c=="*"):
    print(a*b)
elif(c=="/"):
    print(a/b)
elif(c=="%"):
    print(a%b)
else:
    print("invalid")