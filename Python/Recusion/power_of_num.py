def power(b,p):
    if p==0:
        return 1
    else:
        return b*power(b,p-1)
x = int(input("enter base:"))
y = int(input("enter power:"))
print(f"{x} to the power {y} is = ",power(x,y))