def  f1():
    print('f1')
    return True
    
def  f2():
    print('f2')
    return True

if f1():
    print("a")
elif f2():
    print("b")
else:
    print("c")
    
