a = int(input("enter a number:"))
for i in range(1,a+1):
    print(f"{chr(i+64)} "*i, end = " " )
    print()