def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
a = int(input("enter number:"))
y = fact(a)
print(f"factorial of the number {a} is {y}")