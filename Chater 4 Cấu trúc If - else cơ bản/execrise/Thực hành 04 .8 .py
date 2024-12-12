import math

# Giá của các mặt hàng
H1 = 100000
H2 = 150000
H3 = 120000 
H4 = 90000
H5 = 130000
H6 = 140000

# Nhập số lượng các mặt hàng từ bàn phím
a, b, c, d, e, f = map(int, input("Nhập lần lượt số lượng 6 mặt hàng: ").split())

# Tính tổng tiền
tong_tien = (a * H1) + (b * H2) + (c * H3) + (d * H4) + (e * H5) + (f * H6)

# Áp dụng các chương trình khuyến mại
def tinh_khuyen_mai(tong_tien, a, b, c, d, e, f):
    so_luong_tong = a + b + c + d + e + f
    giam_gia = 0

    # Khuyến mại giảm 20k nếu số lượng món đồ >= 4
    if so_luong_tong >= 4:
        if f >= 2:
            giam_gia = 40000  # Nếu thỏa mãn cả (1) và (2) thì giảm 40k
        else:
            giam_gia = 20000

    # Khuyến mại giảm 30k nếu có mã hàng số 6 với số lượng >= 2
    elif f >= 2:
        giam_gia = 30000

    # Khuyến mại giảm 10% nếu tổng tiền > 500k
    if tong_tien > 500000:
        tong_tien *= 0.9
    
    # Trừ tiền giảm giá vào tổng tiền
    tong_tien -= giam_gia

    # Khuyến mại giảm 15% nếu thoả mãn cả (1) và (3) hoặc (2) và (3)
    if (so_luong_tong >= 4 and tong_tien > 500000) or (f >= 2 and tong_tien > 500000):
        tong_tien *= 0.85
    
    # Khuyến mại giảm 20% nếu thoả mãn cả (1), (2) và (3)
    if so_luong_tong >= 4 and f >= 2 and tong_tien > 500000:
        tong_tien *= 0.8
    
    return tong_tien

# Tính số tiền sau khi áp dụng khuyến mại
tong_sau_khuyen_mai = tinh_khuyen_mai(tong_tien, a, b, c, d, e, f)

# In kết quả
print(f"Số tiền phải trả: {tong_sau_khuyen_mai}đ")
