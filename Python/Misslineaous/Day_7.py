""" def pallendrom(n):
    return n[::-1]==n
print (pallendrom("radar")) """

""" def bipin(*a):
    s = 0
    for i in a:
        s+=i
        print(s)
bipin(4,5) """
""" x = 20
def outera():
    x = 10
    def inner():
        x=5
        print(x)
    return inner()
y = outera() """
        
    
""" def even(l):
    n = []
    for i in l:
        if i%2==0:
            n.append(i)
    return n
a = [1,2,3,4,5,6,7,8,9,10]
y = even(a) 
print(y) """

"""def name():
    return "santosh"
def outer(n):
    def inner():
        x  = name()
        print ("hi",x)
    return inner()
outer(name) """

""" def one(msg):
    return msg+'1'
def two(msg):
    return msg+'2'
def three(fun):
    x = fun("message inside")
    print(x)
three(one)
three(two) """

""" def add(n):
    if n==1:
        return 1
    else:
        return n+add(n-1)
y = add(5)
print(y) """

""" def revrs(s):
    if len(s)==1:
        return s
    return revrs(s[1:])+ s[0]
a = input("enter a string:")
print(revrs(a)) """

""" def add_list(l1):
    if len(l1)==1:
        return l1[0]
    else:
        return add_list(l1[1:])+l1[0]

l = [1,5,7,2,6,8]
print(add_list(l)) """

""" def multi(a,b):
    if b == 0:
        return 0
    
    elif b>0:
        return a + multi(a,b-1)
    else:
        return -multi(a,-(b)) 
a = int(input("enter value of a:"))
b = int(input("enter value of b:"))
c = multi(a,b)
print(c) """

""" def count(s,ch):
    c = 0
    if len(s)==0:
        return 0
    else:
        if s[0]==ch:
            return 1 + count(s[1:],ch)
        else:
            return count(s[1:],ch)
a = input("enter string:")
b = input("enter charecter:")
print(f"{b} is repeted in the string {a} {count(a,b)} times")
 """
""" for i in range (2,100):
    prime = 1
    n = 2
    while(n<i):
     if i%n==0:
      prime = 0
      break
     else:
        n+=1
    if(prime==1):
        print(i) """
    
""" y = lambda a:a*a
n = int(input("enter a integer value:"))
print(f"square of the number {n} is {y(n)}") """

""" y = lambda per:"A"if per>=90 else("B"if per>=80 else ("C" if per>=70 else "fail"))
a = int(input("enter percentage:"))
print("grade is:",y(a)) """
def name(n):
    return n+1
l = [1,2,3,4]
y = list(map(name,l))
print(y)
    
    