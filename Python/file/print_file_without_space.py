f = open(r'C:\Users\Bipin Chaudhary\Documents\fil.txt','r')
c = f.read()
S = 0
for i in c:
    if (i !=" " and i !="."):
        S=S+1
    else:
        S=S
print(S)
f.close()
