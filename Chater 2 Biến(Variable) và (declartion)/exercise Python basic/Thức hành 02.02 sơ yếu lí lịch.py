# Viết chương trình nhập từ bàn phím các thông tin sau và tạo ra các biến để lưu giá trị tương ứng
# Tên
# Năm sinh
# Quê quán
# Chiều cao (m)
# Cân nặng (kg)
# Kết quả tốt nghiệp THPT
# In ra tờ khai Sơ yếu lí lịch tương ứng với các dữ liệu đã nhập. Kết quả chạy được cần giống như hình minh họa

name = input("Nhap ho ten:")
age = input("Nhap nam sinh:")
home_town = input("Nhap que quan:")
height = input("Nhap chieu cao:")
weight = input("Nhap can nang:")
graduate = input("Nhap ket qua tot nghiep:")

print("\n**********************************")
print("******* SO YEU LY LICH ***********")
print("**********************************")

print(
    f"Ho ten:{name} \nNam sinh:{age} \nQue quan:{home_town} \nChieu cao:{height} \nCan nang:{weight} \nTot nghiep loai:{graduate}"
)

print("**********************************")
