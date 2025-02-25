def count(s,ch):
    if len(s)==0:
        return 0
    else:
        if s[0]==ch:
            return 1 + count(s[1:],ch)
        else:
            return count(s[1:],ch)
a = input("enter string:")
b = input("enter charecter:")
print(f"{b} is repeted in the string {a} {count(a,b)} times")