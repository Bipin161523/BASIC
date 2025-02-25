def check_string(n):
    if type(n)==str:
        return True
l = [1,'p',2,'y','t']
y = list(filter(check_string,l))
print(y) 