a = int(input("enter math marks:"))
b = int(input("enter physics marks:"))
c = int(input("enter chemistry marks:"))
d = input("enter branch:")
per = ((a+b+c)/300)*100
if((per>=90)and((d.lower()) in "it,cs")):
    print("you are eligible")
else:
    print("you are not eligible")
    