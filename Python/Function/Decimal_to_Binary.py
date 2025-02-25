def bin(n):
    b = ""
    while(n>0):
        r = n%2
        n = n//2
        b = b+str(r)
    return b[::-1]
a = int(input())
print(bin(a))