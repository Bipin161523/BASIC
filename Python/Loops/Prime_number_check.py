n = int(input("enter a number:"))
while(n<=0):
    print("please input appropriate number:")
    break
x = 1
i = 2
while(i<n):
    if(n%i==0):
     print("it is not prime")
     break
     i+=1
    else:
        print("it is prime")
        break