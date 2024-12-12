# Viết chương trình nhập 3 cạnh tam giác, in ra diện tích tam giác đó.
# Cho trước công thức tính diện tích tam giác như hình 1
# Chương trình cần chạy được như hình 2

import math

a = float(input("Enter a :"))
b = float(input("Enter b :"))
c = float(input("Enter c :"))

#p là nửa chu vi của tam giác

p = (a+b+c)/2

#S là diện tích và độ dài 3 canh tạm giác

S = math.sqrt(p*(p-a)*(p-b)*(p-c))

print("Dien tich tam giac la :",S)




