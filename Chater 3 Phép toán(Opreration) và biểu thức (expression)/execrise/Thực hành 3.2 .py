#Viết chương trình nhập bán kính, in ra chu vi và diện tích hình tròn.
#Biết số Pi = 3.14
#Chương trình cần chạy được như hình minh họa

import math

r = input("Nhap ban kinh :")

pi = 3.14

chuvi = 2*pi*float(r)

dientich =pi*float(r)*float(r)

print("Chu vi hinh tron la : ",chuvi)
print("Dien tich hinh tron la : ",dientich)