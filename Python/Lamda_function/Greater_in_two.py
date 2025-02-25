y = lambda a,b:a if a>b else b
a = int(input("enter first number:"))
b = int(input("enter second number:"))
print(f"grater number among {a} and {b} is {y(a,b)}")