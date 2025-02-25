y = lambda per:"A"if per>=90 and per<=100 else("B"if per>=80 and per<=100 else ("C" if per>=70 and per<=100 else "fail"))
a = int(input("enter percentage:"))
print("grade is:",y(a))