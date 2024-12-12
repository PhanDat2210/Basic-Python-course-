import math

# Nhập điểm các môn
toan, ly, hoa, van, anh, su, dia = map(float, input("Nhập tất cả điểm của mỗi môn Toán, Lý, Hóa, Văn, Anh, Sử, Địa (cách nhau bởi dấu ','): ").split(","))

# Tính tổng điểm trung bình
tong_diem_tb = (toan + ly + hoa + van + anh + su + dia) / 7

# Kiểm tra điểm có hợp lệ hay không
if toan > 10 or ly > 10 or hoa > 10 or van > 10 or anh > 10 or su > 10 or dia > 10 or toan < 0 or ly < 0 or hoa < 0 or van < 0 or anh < 0 or su < 0 or dia < 0:
    print("(", toan, ly, hoa, van, anh, su, dia, ") -> Điểm không hợp lệ")
else:
    # Kiểm tra loại Giỏi
    if tong_diem_tb >= 8.0 and toan >= 4.0 and ly >= 4.0 and hoa >= 4.0 and van >= 4.0 and anh >= 4.0 and su >= 4.0 and dia >= 4.0:
        print("(", toan, ly, hoa, van, anh, su, dia, ") -> Giỏi")
    # Kiểm tra loại Khá
    elif tong_diem_tb >= 6.5 and tong_diem_tb < 8 and toan >= 3.0 and ly >= 3.0 and hoa >= 3.0 and van >= 3.0 and anh >= 3.0 and su >= 3.0 and dia >= 3.0:
        print("(", toan, ly, hoa, van, anh, su, dia, ") -> Khá")
    # Kiểm tra loại Trung Bình
    elif tong_diem_tb >= 4.0 and tong_diem_tb < 6.5:
        print("(", toan, ly, hoa, van, anh, su, dia, ") -> TB")
    # Nếu không thỏa mãn các điều kiện trên, thì xếp loại Yếu
    else:
        print("(", toan, ly, hoa, van, anh, su, dia, ") -> Yếu")
