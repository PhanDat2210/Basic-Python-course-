import math
x = [2,3,4] #unpack

y = {'a':1,'b':2,'c':3}


def hello (a,b,c):
    return a*b*c
hi = lambda a,b,c =1: a*b*c

#print(hi(c=2,b =3)) # key word argument
#print(hello(1,2,3))
#- Kĩ thuật variadict parameter

#default parameter / optional parameter
#print(hello(*x)) #unpack
#print(hello(**y)) #unpack

print(hi(2,3)) # lambda

def hello1(f,*x):
    print(len(x),sum(x))
    return math.prod(x) *f
hi = lambda *x: math.prod(x)
print(hello1(0.5,2,3,4))

print(hi(1,2,3))

def hello2(f,a,b,c):
    print(len(x),sum(x))
    return math.prod(x) *f
hi = lambda *x: math.prod(x)

x = [1,2,3]
print(hello2(0.5,*x))

print(hi(1,2,3))

