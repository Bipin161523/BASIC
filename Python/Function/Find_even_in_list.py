def even(l):
    for i in l:
        if i%2==0:
            print(i)
a = [1,2,3,4,5,6,7,8,9,10]
y = even(a)



def even(l):
    n = []
    for i in l:
        if i%2==0:
            n.append(i)
    return n
a = [1,2,3,4,5,6,7,8,9,10]
y = even(a) 
print(y)