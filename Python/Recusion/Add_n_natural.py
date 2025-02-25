def add(n):
    if n==1:
        return 1
    return n+add(n-1)
a = int(input("enter the end value:"))
print(f"addition of first {a} natural number is", add(a))