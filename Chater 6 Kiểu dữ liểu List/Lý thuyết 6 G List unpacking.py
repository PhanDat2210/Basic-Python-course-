#Lý thuyết 06.G [optional] - List unpacking : mở gói
x = [1,2,3]
x1,x2,x3 = x
print(x1,x2,x3)

x,y,z = input("Nhap day so :").split()

print(type(x).__name__, type(y),type(z))
