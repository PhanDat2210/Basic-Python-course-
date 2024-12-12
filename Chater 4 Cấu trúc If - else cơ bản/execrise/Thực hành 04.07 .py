a, b, c = map(float, input("Nhập 3 cạnh tam giác (cách nhau bằng khoảng trắng): ").split())

# Điều kiện là tam giác:
# 1: Tổng 2 cạnh bất kỳ luôn lớn hơn 2 cạnh còn lại
if a + b > c and a + c > b and b + c > a:
    # Cân: Khi có 2 cạnh bằng nhau
    condition1 = ("Kết quả 2: Không phải tam giác cân", "Kết quả 2: Tam giác cân")[a == b or b == c or a == c]

    # Đều: Khi có 3 cạnh bằng nhau
    condition2 = ("Kết quả 3: Không phải tam giác đều", "Kết quả 3: Tam giác đều")[a == b == c]

    # Vuông: khi bình phương 1 cạnh bằng xấp xỉ tổng của bình phương 2 cạnh còn lại. Độ lệch xấp xỉ cho phép < 1
    condition3 = ("Kết quả 4: Không phải tam giác vuông",
                  "Kết quả 4: Tam giác vuông")[abs(a**2 + b**2 - c**2) < 1 or
                                              abs(a**2 + c**2 - b**2) < 1 or
                                              abs(b**2 + c**2 - a**2) < 1]

    # Vuông cân: Khi vừa thỏa mãn điều kiện vuông và điều kiện cân
    condition4 = ("Kết quả 5: Không phải tam giác vuông cân",
                  "Kết quả 5: Tam giác vuông cân")[(a == b or b == c or a == c) and
                                                  (abs(a**2 + b**2 - c**2) < 1 or
                                                   abs(a**2 + c**2 - b**2) < 1 or
                                                   abs(b**2 + c**2 - a**2) < 1)]

    # Phân loại tam giác
    if condition4 == "Kết quả 5: Tam giác vuông cân":
        print(condition4)
    elif condition3 == "Kết quả 4: Tam giác vuông":
        print(condition3)
    elif condition2 == "Kết quả 3: Tam giác đều":
        print(condition2)
    elif condition1 == "Kết quả 2: Tam giác cân":
        print(condition1)
    else:
        print("Kết quả 6: Tam giác thường")  # Tam giác thường nếu không thuộc các loại trên
else:
    print("Kết quả 1: Tam giác này không tồn tại")


# cách 2:
def kiem_tra_tam_giac(a, b, c):
    # Kiểm tra điều kiện tam giác tồn tại
    if a + b > c and a + c > b and b + c > a:
        # Kiểm tra tam giác đều (3 cạnh bằng nhau)
        if a == b == c:
            return "Tam giác đều"
        
        # Kiểm tra tam giác vuông với độ lệch xấp xỉ < 1
        is_vuong = abs(a**2 + b**2 - c**2) < 1 or abs(a**2 + c**2 - b**2) < 1 or abs(b**2 + c**2 - a**2) < 1
        
        # Kiểm tra tam giác cân (2 cạnh bằng nhau)
        if a == b or b == c or a == c:
            # Kiểm tra nếu đồng thời là tam giác vuông cân
            if is_vuong:
                return "Tam giác vuông cân"
            return "Tam giác cân"
        
        # Nếu là tam giác vuông nhưng không cân
        if is_vuong:
            return "Tam giác vuông"
        
        # Nếu không thỏa mãn các điều kiện trên, là tam giác thường
        return "Tam giác thường"
    else:
        return "Ba cạnh này không tạo thành tam giác."

# Nhập 3 cạnh của tam giác
a, b, c = map(float, input("Nhập 3 cạnh tam giác (cách nhau bằng khoảng trắng): ").split())

# Kiểm tra và in kết quả
ket_qua = kiem_tra_tam_giac(a, b, c)
print(ket_qua)
