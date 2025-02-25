def remove_set(s,n):
    s.remove(n)
    return s
l = {1,2,3,1,2,3}
a = int(input())
print(remove_set(l,a))