""" def bipin(x):
    return int(x)
a = input("Enter number seprated by space:").split( )
y = list(map(bipin,a))
print(y) """

a = input("Enter number seprated by space:").split( )
y = list(map(int,a))
print(y)