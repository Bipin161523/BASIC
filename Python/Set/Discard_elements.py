def discart_set(s,n):
    s.discard(n)
    return s
l = {1,2,3,1,2,3}
print(discart_set(l,3))