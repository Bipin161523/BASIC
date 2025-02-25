a = int(input("enter a number:"))
r  = 0
rev = 0
n = a
while(a>0):
    r = a%10
    rev = rev*10+r
    a = a//10
if(rev == n):
 print(" it is a pallendom digit") 
else:
    print("not it is not pallandrom")