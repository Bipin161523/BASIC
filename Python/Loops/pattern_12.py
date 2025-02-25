a = int(input("enter a number:"))
c = 0
for i in range (1,a+1):
    for j in range(1,i+1):
        c=c+1
        print(c,end = " ")
    print()