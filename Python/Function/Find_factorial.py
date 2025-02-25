def fact(n):
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