""" a = input("Enter a number:") 
print(a.capitalize()) """
""" def bipin(n):
    return n.capitalize()
l = ['san','fan','ran']
y = list(map(bipin,l))
print(y) """
""" def strlower(n):
    return n.lower()
l = ['BIPIN','CHAUDHARY','AKASH','AMIT','ANUJ','SHIVANG']
Y = list(map(strlower,l))
print(Y) """
""" def strlower(n):
    return n.title()
l = ['bipin','chaudhary','akash','amit','anuj','shivang']
Y = list(map(strlower,l))
print(Y) """



""" def short(st):
    return st.lower()
def big(St):
    return St.upper()
def cap(p):
    return p.capitalize()
def subfind(m,ch):
    y = m.find(ch)
    if y==-1:
        print("NA")
    else:
        print(f"your alphabet in name on {y+1} position")
def tit(v):
    return v.title()
def d(m,n):
    return m.index(n) 
def cnt(m,n):
    return m.count(n) 
def k(m):
    return m.split(" ")
def l(m,n,q):
    return m.replace(n,q)
def h(m,n):
    return m.rsplit(",",n)
def j(m,n):
    return m.startswith(n)
def g(m,n):
    return m.endswith(n)
def kl(m):
    return m.isalpha()
def jk(m):
    return m.isdigit()
def bc(m):
    return m.isalnum() 
def cc(m):
    return m.isspace()
ch = 'y'
while(ch=='y'):
    print("0th for title:")
    print("1st for lower:")
    print("2nd for upper:")
    print("3rd for captilize your name:")
    print("4th for searching alphabet in name:")
    print("5th for searching alphabet index in name:")
    print("6th for count letter in word:")
    print("7th for split into list:")
    print("8th for replace alphabet in word:")
    print("9th for split from right side:")
    print("10th for check sting fro starting with:")
    print("11th for check sting from end with:")
    print("12th for check string alphabet type")
    print("13th for check string digit type")
    print("14th for check string numeric type")
    print("15th for check space")
    op = input("enter your option:")
    if(op=='1'):
        t = input("enter your text for lower:")
        y = print(short(t))
    elif(op=='2'):
        t = input("enter your text for upper:")
        y = print(big(t))
    elif(op=='3'):
        t = input("enter your name for captilize:")
        y = print(cap(t))
    elif(op=='4'):
        m = input("enter name for search:")
        ch = input("enter alphaber:")
        y = subfind(m,ch)
    elif(op=='5'):
         m = input("enter name for search for index:")
         n = input("enter alphaber:")
         y = print("index is ",d(m,n))
    elif(op == '0'):
        t = input("enter your name for title:")
        print(tit(t))
    elif(op=='6'):
         m = input("enter name :")
         n = input("enter letter:")
         y = print("no of letter in word is ",cnt(m,n))
    elif(op=='7'):
        m = input("enter name to be split:")
        y = print(k(m))
    elif(op=='8'):
         m = input("enter name :")
         n = input("enter letter which to be removed:")
         q = input("enter letter which to be put:")
         print(l(m,n,q))
    elif(op=='9'):
        m = input("enter name to be split from right side:")
        n = int(input("enter number of string to split:"))
        y = print(h(m,n))
    elif(op=='10'):
         m = input("enter name :")
         n = input("enter prefix:")
         y = print(j(m,n))
    elif(op=='11'):
         m = input("enter name :")
         n = input("enter suffix:")
         y = print(g(m,n))
    elif(op=='12'):
        m = input("enter any string:")
        y = print(kl(m))
    elif(op=='13'):
        m = input("enter any string:")
        y = print(jk(m))
    elif(op=='14'):
        m = input("enter any string:")
        y = print(bc(m))
    elif(op=='15'):
        m = input("enter any string:")
        y = print(cc(m))
        
    else:
        print("enter valid option:")
        break
    ch = input("do u want to continue enter (y/n)").lower()
    print("Thanks for using the progrram") """


m = []
l = [1,2,3,4,5,6,7,8,9,10]
n = len(l)
for i in range (n-1,-1,-1):
    if(l[i]%2==0):
        y = l.pop(i)
        m.append(y)
print(m[::-1])
print(l)
