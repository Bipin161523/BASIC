def even(n):
    if n%2==0:
        return True
l = [1,2,3,4,5,6,7,8,9,10]
y = list(filter(even,l))
print(y)