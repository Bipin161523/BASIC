a = int(input("Enter x coordinat:"))
b = int(input("Enter y coordinate:"))
if(a>0 and b>0):
    print("first coordinate")
elif(a>0 and b<0):
     print("fourth coordinate")
elif(a<0 and b>0):
        print("second coordinate")
elif(a<0 and b<0):
        print("third coordinate")
elif(a==0 and b!=0):
    print("point is on y-axis")
elif(a!=0 and b==0):
    print("point is on x-axis")
else:
    print("it is 0,0 point")
    