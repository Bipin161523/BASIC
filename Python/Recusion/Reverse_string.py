def revrs(s):
    if len(s)==1:
        return s
    return revrs(s[1:])+ s[0]
a = input("enter a string:")
print(revrs(a))