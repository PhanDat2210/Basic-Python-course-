def process_names(set1, set2):
    """
    Processes two sets of full names, extracts common names, unique names, and a unique list of first names.

    Args:
        set1 (set): The first set of full names.
        set2 (set): The second set of full names.

    Returns:
        tuple: A tuple containing sets of common names, unique names, and unique first names.
    """

    # Tìm các họ tên chung giữa hai set
    common_names = set1.intersection(set2)

    # Tìm các họ tên chỉ xuất hiện ở 1 trong 2 set
    unique_names = set1.symmetric_difference(set2)

    # Tách và thu thập tên riêng (lược bỏ họ và tên đệm)
    all_first_names = []
    for name in set1 | set2:  # Duyệt qua tất cả các họ tên trong set
        first_name = name.split()[-1].strip()  # Lấy tên riêng (phần cuối)
        all_first_names.append(first_name)

    unique_first_names = set(all_first_names)  # Loại bỏ trùng lặp

    return common_names, unique_names, unique_first_names

# Nhập dữ liệu từ người dùng
a_str = input("Nhập set tên a (tách bởi dấu chấm phẩy ';'): ")
b_str = input("Nhập set tên b (tách bởi dấu chấm phẩy ';'): ")

# Chuyển đổi chuỗi nhập thành set họ tên
a = set(a_str.split(";"))
b = set(b_str.split(";"))

# Xử lý và lấy kết quả
common_names, unique_names, unique_first_names = process_names(a, b)

# In kết quả
print("Kết quả 1 - Các họ tên xuất hiện ở cả 2 set:", ", ".join(common_names))
print("Kết quả 2 - Các họ tên chỉ xuất hiện ở 1 trong 2 set:", ", ".join(unique_names))
print("Kết quả 3 - List các tên (không lặp):", ", ".join(unique_first_names))
