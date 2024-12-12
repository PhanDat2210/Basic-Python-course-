import math

a = int(input("Enter a: "))
b = int(input("Enter b: "))

def tim_UCLN(a,b):
    #Sử dụng hàm gcd (greatest common divisor) của thư viện math.
    return math.gcd(a,b)
def tim_BCNN(a,b):
    #Sử dụng hàm lcm (least common multiple) của thư viện math.
    return math.lcm(a,b)
#Công thức: BCNN(a, b) = |a * b| / UCLN(a, b)

print("UCLN = ",tim_UCLN(a,b))
print("BCNN = ",tim_BCNN(a,b))
