m = []
l = [1,2,3,4,5,6,7,8,9,10]
n = len(l)
for i in range (n-1,-1,-1):
    if(l[i]%2==0):
        y = l.pop(i)
        m.append(y)
print(m[::-1])
print(l)
