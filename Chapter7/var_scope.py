from dis import dis

def f1(a):
    print(a)
    print(b)

dis(f1)

#################################################
print('#' * 50)

b = 6
def f2(a):
    print(a)
    print(b)
    b = 9

dis(f2)
