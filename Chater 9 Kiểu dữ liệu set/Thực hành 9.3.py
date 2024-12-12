# Danh sách các set số nguyên
a = {0, 1, 2, 3, 4, 5, 6, 7, 12}
b = {0, 2, 4, 6, 8, 10}
c = {0, 3, 6, 9, 12}
d = {0, 1, 3, 5, 6, 7, 9, 11, 12}
e = {10, 9, 6, 0, 1, 2, 5}

x = [a, b, c, d, e]

# 1 - Tập các phần tử chung xuất hiện trong tất cả các set
common_elements = set.intersection(*x)

# 2 - Độ dài lớn nhất của set
max_length = max(len(s) for s in x)

# 3 - Phần tử nhỏ nhất trong tất cả các set
min_element = min(min(s) for s in x)

# 4 - Giá trị trung bình của tất cả các phần tử trong các set
all_elements = set.union(*x)
average_value = sum(all_elements) / len(all_elements)

# 5 - Tìm tập các phần tử chỉ xuất hiện trong đúng 2 set
from collections import Counter

element_counts = Counter()
for s in x:
    element_counts.update(s)

two_occurrence_elements = {element for element, count in element_counts.items() if count == 2}

# In kết quả
print("Kết quả 1: ", common_elements)
print("Kết quả 2: ", max_length)
print("Kết quả 3: ", min_element)
print("Kết quả 4: ", int(average_value))  # Làm tròn giá trị trung bình
print("Kết quả 5: ", sorted(two_occurrence_elements))
