ten_nguoi1 = input("nhap ten nguoi 1 :")
ten_nguoi2 = input("nhap ten nguoi 2 :")
if len(ten_nguoi1) > len(ten_nguoi2):
    print(f"kết quả 1:{ten_nguoi1}")
else:
    print(f"kết quả 1:{ten_nguoi2}")
ky_tu_giong_nhau = set(ten_nguoi1) & set(ten_nguoi2)
ky_tu_giong_nhau = sorted(list(ky_tu_giong_nhau))
print(f"kết quả 2:{' '.join(ky_tu_giong_nhau)}")

ten_nguoi_1_bo_ho_dem = ten_nguoi1.split()[-1]
ten_nguoi_2_bo_ho_dem = ten_nguoi2.split()[-1]
print(f"kết quả 3:{ten_nguoi_1_bo_ho_dem}{ten_nguoi_2_bo_ho_dem}")

ten_nguoi_1_bo_ho_dem = ten_nguoi1.title()
ten_nguoi_2_bo_ho_dem = ten_nguoi2.title()
if ten_nguoi_1_bo_ho_dem < ten_nguoi_2_bo_ho_dem:
    print(f"kết quả 4:{ten_nguoi_1_bo_ho_dem}")
else:
    print(f"kết quả 4:{ten_nguoi_2_bo_ho_dem}")

"""Thực hành 08.02
Nhập 2 chuỗi kí tự tên người
1. In ra chuỗi kí tự dài hơn (có nhiều kí tự hơn)
2. Thống kê các kí tự chữ cái giống nhau giữa 2 tên 
3. In ra tên của 2 người nhưng bỏ đi phần họ và tên đệm  (nếu có )
4. Kiểm tra xem tên của ai đứng trước nếu xếp theo danh sách ABC. Chú ý: 
Khi sắp xếp danh sách tên, người ta ko tính họ và tên đệm. 
[Ví dụ]
Nhap ten nguoi 1: Nguyen Anh Vu 
Nhap ten nguoi 2: Truong Xuan An 
Ket qua 1: Nguyen Anh Vu
Ket qua 2: A g n u 
Ket qua 3: Vu An 
Ket qua 4: Truong Xuan An"""
