a = int(input("enter a number:"))
s = 0
r = 0
while(a>0):
    r=a%10
    s+=r
    a=a//10
print(s)