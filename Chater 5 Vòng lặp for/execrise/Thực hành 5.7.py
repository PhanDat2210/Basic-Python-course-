import math

def f(x):
    if x >= 5 :
        return 2*x**2 + 5*x + 9
    else :
        return -2*x**2 + 4*x - 9  
def sum_f(n):
    tong = 0
    for i in range(1,n+1):
        tong +=f(i)
    return tong

n = int(input("Nhập n: "))

result = sum_f(n)

print(f"Ket qua:{result}")
