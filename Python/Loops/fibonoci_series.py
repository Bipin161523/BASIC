n = int(input("enter a number:"))
a , b = 0,1
if(n<=0):
    print("please input positive number:")
else:
    print("Fabonoci series:")
    
    for i in range(n):
        print(a, end = " ")
        a,b = b,a+b