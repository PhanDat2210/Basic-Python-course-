
#Nhập vào số nguyên dương n từ bàn phím.
#Kiểm tra xem n có phải là số chính phương hay không? (số chính phương là số khi lấy căn bặc 2 có kết quả là nguyên).

import math

n = float(input("Nhap n: "))
Ket_qua = ("Ket qua : n ko phai so chinh phuong","Ket qua : n la so chinh phuong")[math.sqrt(n) == int(math.sqrt(n))]

print(Ket_qua)