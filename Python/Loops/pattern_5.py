a = int(input("enter a number:"))
for i in range(1,a+1):
    for j in range(1,a+1):
        print(chr(i+64), end = " ")
    print()