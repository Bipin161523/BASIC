n = int(input("enter a number:"))
t= len(str(n))
r  = 0
rev = 0
while(n>0):
    r = n%10
    n = n//10
    rev = rev+r**t
    t = t-1
print(rev)
