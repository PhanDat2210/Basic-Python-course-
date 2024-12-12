# Lý thuyết 06.F [*] - Kỹ thuật List comprehension

# Cấu trúc cho phép tạo ra một list mới dựa trên 1 list gốc một cách ngắn gọn và nhanh chóng
x = input("Nhap day so :").split()
# y= []
# or item in x :
#  y.append(int(item))
# print(type(x), " ", x)
#print(y)
y =[int(item) * int(item) for item in x if int(item)%2==0]

print(y)
