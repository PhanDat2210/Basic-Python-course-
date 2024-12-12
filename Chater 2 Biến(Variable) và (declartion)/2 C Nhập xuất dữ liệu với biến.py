# Lý thuyết 02.C - Nhập xuất dữ liệu với biến

ho_ten = input("Nhập tên: ")
tuoi = input("Nhập tuổi: ")
chieu_cao, can_nang = input("Nhập chiều cao, cân nặng: ").split(
    " "
)  # .split(",") là cắt ra tên, tên, chiều cao, cân nặng
# print("Người vừa nhập: ", HO_TEN,"Anh ấy rất quach tỉnh và đẹp trai.Năm nay anh ấy :", tuoi)
print(
    f"Người vừa nhập: , {ho_ten},Anh ấy rất quach tỉnh và đẹp trai.Năm nay anh ấy :, {tuoi}"
)
print("Xin chào! ",end ='-> ')
print(
    f"Chiều cao: {chieu_cao} Cân nặng: {can_nang}", sep=""
)  # seperator dấu ngăn các phần tên bao gì nhau
