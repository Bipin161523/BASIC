def multi(a,b):
    if b == 0:
        return 0
    
    elif b>0:
        return a + multi(a,b-1)
    else:
        return -multi(a,-(b)) 
a = int(input("enter value of a:"))
b = int(input("enter value of b:"))
c = multi(a,b)
print(c)