#Viết chương trình nhập 2 số thực x, y từ bàn phìm. x, y.
#1 - Kiểm tra chúng có khác 0 hay ko và in kết quả ra màn hình.
# - Nếu x,y khác 0. Kiểm tra tiếp xem chúng có cùng dấu hay khác dấu và in kết quả ra màn hình

x = float (input("Nhap  x : "))
y = float (input("Nhap  y : "))

# 1 - Kiểm tra xem x và y có khác 0 hay không và in kết quả
if x ==0:
    print("x bang 0")
else:
    print("x khac 0")
if y ==0:
    print("y bang 0")
else:
    print("y khac 0")

# - Nếu x, y khác 0. Kiểm tra tiếp xem chúng có cách dấu hay khác dấu và in kết quả ra môn hình
if x!= 0 and y!=0:
    if (x > 0 and y > 0) or (x < 0 and y < 0):
        print("Hai so cung dau")
    else :
        print("Hai so trai nhau")