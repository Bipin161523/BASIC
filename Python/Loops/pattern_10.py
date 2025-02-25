a = int(input("enter a number:"))
for i in range (1,a+1):
    for j in range(1,a-i+1):
        print(chr(64+j),end = " ")
    print()