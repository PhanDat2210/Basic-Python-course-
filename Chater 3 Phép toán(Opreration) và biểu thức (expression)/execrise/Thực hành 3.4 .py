# Viết chương trình nhập vào một số có 3 chữ số, in ra số đảo ngược.
# Chương trình cần chạy được như hình minh họa

#n = input("Nhap n :")

# Đảo ngược số bằng cách chuyển số thành chuỗi và dùng slicing

#print("So dao nguoc la :", n[::-1])  # cách 1

# cách 2
# Nhập vào một số nguyên dương
n = int(input("Nhap n: "))

# Biến để lưu kết quả của số đảo ngược
so_dao_nguoc = 0

# Lặp lại cho đến khi n bằng 0
while n > 0:
    # Lấy chữ số cuối cùng của n
    chu_so = n % 10
    # Thêm chữ số vào số đảo ngược
    so_dao_nguoc = so_dao_nguoc * 10 + chu_so
    # Bỏ chữ số cuối cùng của n
    n = n // 10

# In ra số đảo ngược
print("So dao nguoc la:", so_dao_nguoc)
