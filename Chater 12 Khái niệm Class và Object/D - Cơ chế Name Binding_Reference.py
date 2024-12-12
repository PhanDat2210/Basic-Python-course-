import copy

x = [1, 2, 3]
y = copy.copy(x)
print(id(x))
print(id(y))
# name binding : kết nối ,liên kết


a = [1,2,3] # inmutable


def add(number):  # number =x
    number [0 ] = 10
    return number


a = add(a)
print(a)
