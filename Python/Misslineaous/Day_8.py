""" def prime(n):
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
print(l[::2]) """


""" def bin(n):
    b = ""
    while(n>0):
        r = n%2
        n = n//2
        b = b+str(r)
    return b[::-1]
a = int(input())
print(bin(a)) """

""" def sqrt(n):
    return n**2
bipin = [1,2,3,4]
y = list(map(sqrt,bipin))
print(y) """


""" l = [1,2,3,4,5]
y = list(map(lambda n:n+1,l))
print(y)  """ 
""" def inm(n):
    return int(n)
l = ['1','2','3','4']
y = list(map(inm,l))
print(y) """
""" def bipin(x):
    return int(x)
a = input("Enter number seprated by space:").split( )
y = list(map(bipin,a))
print(y) """
""" def stn(n):
    if type(n)==str:
        return True
l = [1,'p',2,'y','t']
y = list(filter(stn,l))
print(y)  """

""" def chek(n):
    if len(n)>=4:
        return True
l = ['mohan','san','sita','santosh']
y = list(filter(chek,l))
print(y) """
""" def Sum(n):
    return sum(n)
l = [1,2,3,4]
print(Sum(l)) """

""" k = int(input("enter range:"))
lst = []
for i in range(1,k):
   lst.append(i)
print(lst)
a = int(input("enter string for append:"))
lst.append(a)
print(lst) """

""" a = input("enter string:")
l = []
for i in a:
    if(i in "aeiouAEIOU"):
        l.append(i)
print(l)      """ 
""" print("input integers:")
l = []
for i in range(1,10):
    l.append(int(input()))
print(l) """

""" lst = [1,2,3,4,5,6]
lst.remove(3)
print(lst) """

""" n = 5
for i in range(1,n+1):
        c = 1
        for j in range(i):
            print(c,end =  " ")
            c = c
        print() """
a = 9
b = 0
try:
    print(a/b)
except Exception as a:
    print(a)