""" for i in range(1,6): #1 2 3 4 5 
    print("Bipin Chaudhary") """
""" for i in range(5):
    print(i)
else:
    print("loop completed") """
""" for i in range(1,11):
    print("*")
    print(i)
print("santo") """

""" for i in range(3):
    for j in range(5):
        print(f"i={i}, j={j}") """
""" a = int(input("enter a number:"))
for i in range(1,11):
    print(f"{a}x{i} =",a*i) """
    
""" for i in range(3): # Outer loop
 for j in range(2): # Inner loop
  print(f"i={i}, j={j}") """

""" for i in range(1,5):
        print("*"*i) """
        
""" for i in range(1,11):
    if(i%2==0):
        print(i) """
""" s = 0
for i in range(1,11):
    s+=i
print(s) """
""" a = int(input("enter a integer:"))
s = 1
for i in range(1,a+1):
    s*=i
print("Factorial of the number is:",s) """

""" l = [1,2,3,4,5]
s = 0
for i in l:
    s+=i
print(s) """

""" l = [32,16,17,52,13,14] 
for i in l:
    if(i%2!=0):
        print(i) """
        
""" l = ['hello','sila','sanlon','geeta','ram']
for i in l:
    if (len(i)>4):
        print(i) """

""" l = ['hello',1,2,3,'ram','sita']
for i in l:
    if(type(i)==str):
        print(i) """

""" a = 0
b = 1
print(a)
print(b)
for i in range(1,11):
    s = a+b
    a = b
    b = s
    print(s) """
""" a,b = 0,1
for i in range(1,10):
    print(a)
    a,b=b,a+b """
    
    
""" a = "santosh gupta"
for i in a:
    if(i in"aeiouAEIOU"):
     print(i, end = " ") """


""" for j in range(1,6):
 for i in range(6-j):
    print("*", end = " ")
 print()  """
 
 
""" rows = int(input("Enter a number: "))
for i in range(1, rows + 1):
   print("*" * (rows-i)) """""" print(" " * (rows - i) + "*" * (2 * i - 1)) """


""" 
a = int(input("enter a number:"))
for i in range(1,a+1):
    for j in range(i):
        print(i, end = " ")
    print()  """
    
""" for i in range(1,6):
    print(f"{i} "*i , end = " ")
    print() """
    
    
""" a = int(input("enter a number:"))
for i in range(1,a+1):
    for j in range(i+1):
     print(f"{chr(i+64)} "*i, end = " " )
     print()  """
     

""" a = int(input("enter a number:")) 
for i in range(1,a+1):
    for j in range(1,a+1):
        print(chr(j+64), end = " ")
    print() """
    
""" a = int(input("enter a number:"))
for i in range (1,a+1):
    for j in range(1,a-i+1):
        print(" ",end = "")
    for k in range(1,2*i):
        print("*",end = "")
    print() """

""" l = ['ram','mohan','sita','akhya']
c = 0
for i in l:
    c = len(i)+c
print(c) """

""" s = 'my name is santosh'
c = 0
for i in s:
    if(i!=" "):
     c+=1
print(c) """

""" l = [[1,2,3,4],[7,6,3,2]]
s = 0
for i in l:
    for n in i:
        s = s+n
print(s) """
""" n = int(input("enter a number:"))
i = 1
while(i<=10):
    print(f"{n}*{i} = ",n*i)
    i+=1
 """
 
f = 1
i = 1
while(i<=5):
    f = f*i
    i+=1
print(f)
    