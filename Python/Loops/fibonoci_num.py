num = int(input("Enter a number:"))
a = 0
b = 1
print(a)
print(b)
for i in range(1,num+1):
    s = a+b
    a = b
    b = s
    print(s)
    
""" a,b = 0,1
for i in range(1,10):
    print(a)
    a,b=b,a+b """