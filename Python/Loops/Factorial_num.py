a = int(input("enter a integer:"))
if(a<0 ):
    print("factorial not exist for neagtive number")
else:
    s = 1
    for i in range(1,a+1):
        s*=i
    print("Factorial of the number is:",s)
