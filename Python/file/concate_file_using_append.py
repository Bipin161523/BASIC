f1 = open(r'C:\Users\Bipin Chaudhary\Documents\bip.txt','r')
a = f1.read()
f2 = open(r'C:\Users\Bipin Chaudhary\Documents\fil.txt','r')
b = f2.read()
f3 = open(r'C:\Users\Bipin Chaudhary\Documents\aka.txt','a')
f3.write(a)
f3.write(b)
print("done")
f1.close()
f2.close()
f3.close()