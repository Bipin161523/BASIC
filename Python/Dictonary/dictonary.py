d = {}
for i in 'hello':
    if i in d:
        d[i]=d[i]+1
    d[i]=1
print(d)