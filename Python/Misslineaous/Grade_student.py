a = int(input("Enter first subject mark:"))
b = int(input("Enter second subject mark:"))
c = int(input("Enter third subject mark:"))
d = int(input("Enter fourth subject mark:"))
e = int(input("Enter fiveth subject mark:"))
per = (a+b+c+d+e)/5
if (per>=90):
    print("A grade")
elif (per>=80):
    print("B grade")
elif (per>=70):
    print("C grade")
elif (per>=60):
    print("d grade")
else:
    print("fail")