k = int(input("enter a integer value:"))
for k in range(1,k):
    k+=1
    t= len(str(k))
    r  = 0
    rev = 0
    n = k
    while(k>0):
            r = k%10
            rev = rev+r**t
            k = k//10
    if(rev == n):
        print(n,end=" ")