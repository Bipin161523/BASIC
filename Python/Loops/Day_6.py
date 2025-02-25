""" rows = int(input("Enter a number: "))
for i in range(1, rows + 1):
 print(" " * (rows - i) + "*" * (2 * i -1)) """
 
""" i = 10
while(i>=5):
 print(i) 
 i-=1 """
""" a = int(input("enter a number:"))
i = 1
while(i<=10):
    print(f"{a}x{i} =",a*i)
    i+=1  """
   
""" s = 0
i = 1
while(i<=10):
    s+=i
    i+=1
print(s) """

""" a = int(input("enter a number:"))
f = 1
while(a>0):
    f*=a
    a-=1
print(f) """

""" a = int(input("enter a number:"))
s = 0
r = 0
while(a>0):
    r=a%10
    s+=r
    a=a//10
print(s) """


""" rows = int(input("Enter a number: "))
for i in range(0,rows):
 print(" " * (rows - i) + "*" * (2 * i - 1))
for j in range(rows-1,0,-1):
    print(" " * (rows-j) + "*" * (2 * j - 1)) """
    

""" for k in range(1,500):
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
        print(n,end=" ") """
        
    
        
    
""" n = int(input("enter a number:"))
a , b = 0,1
if(n<=0):
    print("please input positive number:")
else:
    print("Fabonoci series:")
    
    for i in range(n):
        print(a, end = " ")
        a,b = b,a+b """

""" n = int(input("enter a number:"))
count = 0
while(n>0):
    n=n//10
    count+=1
print(count)  """
""" n = int(input("enter a number:"))
t= len(str(n))
r  = 0
rev = 0
while(n>0):
    r = n%10
    n = n//10
    rev = rev+r**t
    t = t-1
print(rev) """

""" a = 5
if a>5:
 pass
else:
    print("hello") """

""" for a in range(1,10):
    if(a==5 or a==7):
        pass
    print(a) """ 
    


""" n = int(input("enter a number:"))
a,b = 0,1
k = 1
while(k<n):
    print(a)
    a,b=b,a+b
    k+=1 """
        
""" def sum(a,b):
    result = a+b
    return result
x = 5
y = 9
z = sum(x,y)
print(z) """

""" def airthematic(a,b):
    add = a+b
    sub = a-b
    multi = a*b
    div = a//b
    return add,sub,multi,div
a,b,c,d = airthematic(10,5)
print(a,b,c,d) """

""" n = int(input("enter a number:"))
while(n<=0):
    print("please input appropriate number:")
    break

i = 2
while(i<n):
    if(n%i==0):
     print("it is not prime")
     break
     i+=1
    else:
        print("it is prime")
        break """

""" s = 0
for n in range(2,100):
    
    f = 1
    i = 2
    while(i<n):
        if(n%i==0):
         f = 0
         break
        else:
         i+=1
    if(f==1):
         print(i) """
         
         
""" def list(lst):
    lst.append("akash")
    return lst
liste = [1,2,3]
z = list(liste)
print(z) """
        
""" def power(a,b):
    i = 1
    n = a
    while(i<b):
        a*=n
        i+=1
    return a
        
x = int(input("enter base:"))
y = int(input("enter power:"))
t = power(x,y)
print(f"{x} to the power {y} is",t) """


""" def fact(n):
    f = 1
    i = 1
    if(n<=0):
        print("enter only positive value:")
    else:
     while(i<=n):
        f*=i
        i+=1
    return f
x = int(input("enter a number:"))
facto = fact(x)
print(facto)
 """

""" def fun(a,b):
    return (a+b)
y = fun(3,4)
print(type(y))
print(10+y) """

""" def fact(n):
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
print(c) """

""" def math(x,y,o):
    if(o == "+"):
        return x+y
    elif(o=="-"):
        return x-y
    elif(o=="*"):
        return x*y
    elif(o=="//"):
        return x//y
    else:
        return ("enter right opreater")
a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = input("enter opreator")
s =math(a,b,c)
print(s)
 """
        
""" def arm(k):   
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
a = int(input("enter a integer value:"))
arm(a) """
    
    
def arm(n):
    r = 0
    rev = 0
    t = len(str(n))
    tem = n
    while(n>0):
        r = n%10
        rev = rev+r**t
        n = n//10
    if(tem == rev):
        print ("it is armstrong")
    else:
        print("not armstrong")
a = int(input("enter a number:"))
arm(a)

        
    
    
   

