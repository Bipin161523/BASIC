""" def bipin(n):
    return n.capitalize()
l = ['san','fan','ran']
y = list(map(bipin,l))
print(y) """

l = ['san','fan','ran']
y = list(map(str.capitalize,l))
print(y)
