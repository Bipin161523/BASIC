a = input("enter string:")
l = []
for i in a:
    if(i in "aeiouAEIOU"):
        l.append(i)
print(l)     