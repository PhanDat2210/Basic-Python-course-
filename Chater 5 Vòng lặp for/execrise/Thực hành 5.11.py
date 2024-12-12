n = 11  # Số hàng và cột

for i in range(n):
    for j in range(n, 0, -1):
        if j > i + 1:
            # In khoảng trắng cho phần không có số
            print("  ", end=" ")
        elif j == i + 1 or j == n or i == n-1 or j == 1:
            # In số "1" ở viền ngoài
            print("1 ", end=" ")
        else:
            # In số "0" ở giữa
            print("0 ", end=" ")
    print()  # Xuống dòng sau mỗi hàng
