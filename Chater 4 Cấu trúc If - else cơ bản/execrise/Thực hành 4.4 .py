#Nhập vào số giờ, phút, giây từ bàn phím. Kiểm tra xem thời gian nhập vào có hợp lệ hay ko và in kết quả ra màn hình.
#hời gian hợp lệ được quy định như sau: Giờ được tính từ 0 đến 23, phút và giây được tính từ 0 đến 59.

import math

hour = float(input("Enter hour:"))
minute = float(input("Enter minute:"))
second = float(input("Enter second:"))

Return = ("Ket qua : Khong hop le","Ket qua : Hop le")[hour >=0 and hour <=23 and minute >= 0 and minute <=59 and second >=0 and second <=59]

print (Return)