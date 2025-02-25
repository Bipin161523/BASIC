def fact(n):
    f = 1
    i = 1
    while(i<=n):
        f*=i
        i+=1
    return f
n = int(input("enter a integer:"))
r = int(input("enter a integer:"))
f1 = fact(n)
f2= fact(r)
f3 = fact(n-r)
c = f1/(f2*f3)
print(c)