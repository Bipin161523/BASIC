def add_set(s,n):
    s.add(n)
    return s
def discart_set(s,n):
    s.discard(n)
    return s
def intersection_set(s1,s2):
   return s1.intersection(s2)
def union_set(s1,s2):
   return s1.union(s2)
def remove_set(s,n):
    s.remove(n)
    return s
def pop_set(s1,s2):
    s1.pop()
    return s1
def issub_set(s1,s2):
    return s1.issubset(s2)
print("Are you ready for set opreation: then type(Y/N)")
a = input().upper()
while(a =='Y'):
    print("0: for add sets:")
    print("1: for distract set:")
    print("2 for intersection set:")
    print("3: for union sets:")
    print("4:for remove elements:")
    print("5:for pop elements:")
    print("6: for check subset:")
    t = (input("enter option number:"))
    if(t=='0'):
        s1 = set(map(str,input("Enter number seprated by space for s1:").split()))
        s2 = int(input("enter elements"))
        print(add_set(s1,s2))
    elif(t=='1'):
        s1 = set(map(str,input("Enter number seprated by space for s1:").split()))
        s2 = set(map(str,input("Enter number seprated by space for s2:").split()))
        print(discart_set(s1,s2))
    elif(t=='2'):
        s1 = set(map(str,input("Enter number seprated by space for s1:").split()))
        s2 = set(map(str,input("Enter number seprated by space for s2:").split()))
        print(intersection_set(s1,s2))
    elif(t=='3'):
        s1 = set(map(str,input("Enter number seprated by space for s1:").split()))
        s2 = set(map(str,input("Enter number seprated by space for s2:").split()))
        print(union_set(s1,s2))
    elif(t=='4'):
        s1 = set(map(str,input("Enter number seprated by space for s1:").split()))
        s2 = int(input("enter remove number:"))
        print(remove_set(s1,s2))
    elif(t=='5'):
        s1 = set(map(str,input("Enter number seprated by space for s1:").split()))
        s2 = int(input("elements for pop:"))
        print(pop_set(s1,s2))
    elif(t=='6'):
        s1 = set(map(str,input("Enter number seprated by space for s1:").split()))
        s2 = set(map(str,input("Enter number seprated by space for s2:").split()))
        print(issub_set(s1,s2))
    else:
        print("please inter correct option:")
    a = input(("Are you want to proceed more: the press (Y/N)")).upper()
    print("Thanks for using program")
    
    

        