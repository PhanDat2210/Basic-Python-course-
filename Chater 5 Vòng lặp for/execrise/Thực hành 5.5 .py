def la_so_hoan_hao(n):
    """
    Hàm kiểm tra xem n có phải là số hoàn hảo hay không.
    Số hoàn hảo là số có tổng các ước số nhỏ hơn n (không kể chính nó) bằng chính nó.
    """
    # Tính tổng các ước số của n (không kể chính nó)
    tong_uoc_so = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc_so += i

    # Kiểm tra nếu tổng các ước số bằng chính n
    return tong_uoc_so == n


# Nhập một số nguyên dương từ bàn phím
n = int(input("Nhập n: "))

# Kiểm tra và in kết quả
if la_so_hoan_hao(n):
    print(f"{n} là số hoàn hảo.")
else:
    print(f"{n} không phải là số hoàn hảo.")
