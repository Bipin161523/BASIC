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