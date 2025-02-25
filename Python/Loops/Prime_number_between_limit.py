k = int(input("enter a number:"))
for n in range(2,k):
    f = 1
    i = 2
    while(i<n):
        if(n%i==0):
         f = 0
         break
        else:
         i+=1
    if(f==1):
         print(i)
    