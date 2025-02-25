def power(a,b):
    i = 1
    n = a
    while(i<b):
        a*=n
        i+=1
    return a
        
x = int(input("enter base:"))
y = int(input("enter power:"))
t = power(x,y)
print(f"{x} to the power {y} is",t)