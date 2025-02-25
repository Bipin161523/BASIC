def prime(n):
    p = 0
    for i in range(2,n):
        if n%i==0:
            return 1
    return 0
l = []
a = int(input("enter the number limit:"))
for k in range(2,a):
    y = prime(k)
    if(y==0):
        l.append(k)
print(l[::2])