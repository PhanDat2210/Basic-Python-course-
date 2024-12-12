import statistics
import math

n = list(map(int, input("Nhập list :").split()))
# Tính trung bình cộng các số chẵn
chan = [item for item in n if item % 2 == 0]
print(f"Kết quả 1:{statistics.mean(chan)}")

# Tính trung bình cộng các số le
le = [item for item in n if item % 2 == 1]
print(f"Kết quả 2:{statistics.mean(le)}")

# Tính trung bình cộng các số chẵn và le
chan_le = [item for item in n if item % 2 == 0 or item % 2 == 1]
print(f"Kết quả 3:{statistics.mean(chan_le)}")

# 3 - Tìm số lớn nhất trong list vừa nhập
print(f"Kết quả 4:{max(n)}")
print(f"Kết quả 5:{min(n)}")

# Đếm các số chính phương có trong list . Số chính phương là số bằng bình phương của 1 số nguyên. Ví dụ: 4 = 2^2, 9 = 3^2, 25 = 5^2.

# Lọc ra các số chính phương
so_chinh_phuong = [
    number for number in n if number > 0 and math.sqrt(number).is_integer()
]

# Đếm số lượng số chính phương
count = len(so_chinh_phuong)

# In ra số lượng số chính phương
print(f"Kết quả 6:{count}")

# Hiện thị các số nguyên tố có trong list lên màn hình

so_nguyen_to = [
    item
    for item in n
    if item > 1
    and all(item % i != 0 for i in range(2, int(item**0.5) + 1))
    or item == 0
]
print("Kết quả 7:",end="")
for items in so_nguyen_to:
    print(items, end=" ")
n.sort(reverse=False)
print(f"\nKết quả 8:{n}")
