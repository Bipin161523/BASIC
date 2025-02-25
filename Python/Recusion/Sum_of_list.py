def add_list(l1):
    if len(l1)==1:
        return l1[0]
    else:
        return add_list(l1[1:])+l1[0]

l = [1,5,7,2,6,8]
print(add_list(l))