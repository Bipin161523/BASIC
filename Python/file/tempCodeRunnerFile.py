c = f.read()
S = 0
k = 0
for i in c:
    if (i !=" "):
        S=S+1
    else:
        S=S
        k+=1
print(k+1)
f.close()