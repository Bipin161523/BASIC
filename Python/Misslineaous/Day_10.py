""" def add_set(s,n):
    s.add(n)
    return s
l = {1,2,3,1,2,3}
print(add_set(l,7)) """
""" def remove_set(s,n):
    s.remove(n)
    return s
l = {1,2,3,1,2,3}
print(remove_set(l,3)) """
""" def discart_set(s,n):
    s.discard(n)
    return s
l = {1,2,3,1,2,3}
print(discart_set(l,3)) """


""" def pop_set(s):
    s.pop()
    return s
l = {1,'tan'}
print(pop_set(l)) """
""" def intersection_set(s1,s2):
   return s1.intersection(s2)
s1 = {1,2,3,4,5,6}
s2 = {1,2,3,47,8,90}
print(intersection_set(s1,s2)) """
""" a = 0
l = [1,2,3,4,5,6,7,8,1,23,4,2,3,4,5,67,]
s = set(l)
for i in s:
    a+=i
print(a) """
""" l = [1,2,3,4,5,6,7,8,1,23,4,2,3,4,5,67,]
s = set(l)
a = len(s)
print(sum(s)/a) """
""" from functools import reduce
l = [1,2,3,4,5]
a = reduce(lambda x,y:x+y,l)/len(l)
print(a) """

""" d = {'one':1,'two':2,'three':3}
print(d)
print(d["one"],d["three"])
d["two"]=4
print(d)
 """
""" l1 = ['one','two','three']
l2 = [1,2,3]
d = dict(zip(l1,l2))
print(d) """


""" d = {'one':['k','s','d',],'two':2,'three':3}
print(d.update("tw0",0)) """

""" d = {'one':['k','s','d',],'two':2,'three':3}
print(tuple(d.values())) """

""" a = list(map(str,input("enter keys:").split()))
b = list(map(str,input("enter values:").split()))
y = (dict(zip(a,b)))
print(y)
print(list(y.items())) """ 

""" d = {}
for i in 'hello':
    if i in d:
        d[i]=d[i]+1
    d[i]=1
print(d) """
""" a = {'0':1,'t':2,'th':3,'fr':4}
s = 0
for i in a:
    s+=a[i]
print(s) """

""" d1 ={'o':1,'t':2}
d2 ={'th':3,'fo':4}
for i,j in d2.items():
    d1[i]=j
print(d1) """

f1 = open(r'C:\Users\Bipin Chaudhary\Documents\number_check.txt','r')
f2 = open(r'C:\Users\Bipin Chaudhary\Documents\even.txt','w')
f3 = open(r'C:\Users\Bipin Chaudhary\Documents\odd.txt','w')
a = f1.read()
l = a.split(',')
for i in l:
    if(int(i)%2==0):
      f2.write(i)
    else:
        f3.write(i)
print("done")
f1.close()
f2.close()
f3.close()
    

        