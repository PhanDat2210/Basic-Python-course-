def tim_x_nho_nhat(n):
    total = 0
    i = 0
    while total <= n:
        i += 1
        total += i
    return i

# Nhập số nguyên dương n từ bàn phím
n = int(input("Enter n: "))

# Tìm X nhỏ nhất
X_nho_nhat = tim_x_nho_nhat(n)

# In kết quả
print(f"X nhỏ nhất là: {X_nho_nhat}")
