a = input("enter a name:")
a = a.lower()
c = 0
for i in a:
    if(i in "aeiou"):
     print(i)
     c+=1
print(c)