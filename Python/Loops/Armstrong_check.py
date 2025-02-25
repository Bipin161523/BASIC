a = int(input("enter a number:"))
count = 0
while(a>0):               #count digit using len(str(a))
    a=a//10
    count+=1
r  = 0
rev = 0
n = a
while(a>0):
    r = a%10
    rev = rev+r**count
    a = a//10
if(rev == n):
 print("it is armstrong number") 
else:
    print("it is nor a armstrong number") 