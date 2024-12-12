a = [3, 5.5, "ab", 2, "Vu", 0, 6, [2, 3, 4], False, [1, 2], True, 1.13]
a.reverse()
b = tuple(a)
print("Kết quả 1:", [b])
c = []
temp = []
for item in a:
    temp.append(item)
    if len(temp) == 3:
        c.append(tuple(temp))
        temp = []
if temp:
    c.append(tuple(temp))
print("Kết quả 2:", tuple(c))
temp1 = []
for item1 in a:
    for item2 in a:
        if (
            item1 != item2
            and (item1, item2) not in temp1
            and (item2, item1) not in temp1
        ):
            if (
                isinstance(item1, int)
                and isinstance(item2, int)
                and not isinstance(item1, bool)
                and not isinstance(item2, bool)
            ):
                temp1.append((item1, item2))
            elif isinstance(item1, bool) and isinstance(item2, bool):
                temp1.append((item1, item2))
            elif isinstance(item1, float) and isinstance(item2, float):
                temp1.append((item1, item2))
            elif isinstance(item1, str) and isinstance(item2, str):
                temp1.append((item1, item2))
            elif isinstance(item1, list) and isinstance(item2, list):
                temp1.append((item1, item2))
print("Kết quả 3:", tuple(temp1))

a = [3, 5.5, "ab", 2, "Vu", 0, 6, [2, 3, 4], False, [1, 2], True, 1.13]
temp1 = []

for item1 in a:
    for item2 in a:
        if (
            item1 != item2
            and (item1, item2) not in temp1
            and (item2, item1) not in temp1
        ):
            if type(item1) == type(item2):
                temp1.append((item1, item2))

print("Kết quả 3:")
for t in temp1:
    print(f"         {t}")

# Tạo các danh sách để chứa các phần tử cùng kiểu
int_list = []
float_list = []
str_list = []
list_list = []
bool_list = []

# Phân loại các phần tử vào các danh sách tương ứng
for item in a:
    if isinstance(item, int) and not isinstance(
        item, bool
    ):  # Loại trừ bool vì bool là subclass của int
        int_list.append(item)
    elif isinstance(item, float):
        float_list.append(item)
    elif isinstance(item, str):
        str_list.append(item)
    elif isinstance(item, list):
        list_list.append(item)
    elif isinstance(item, bool):
        bool_list.append(item)

# Tạo các tuple từ các danh sách
result = []
if len(int_list) > 1:
    result.append(tuple(int_list))
if len(float_list) > 1:
    result.append(tuple(float_list))
if len(str_list) > 1:
    result.append(tuple(str_list))
if len(list_list) > 1:
    result.append(tuple(list_list))
if len(bool_list) > 1:
    result.append(tuple(bool_list))

# In ra kết quả
print("Kết quả 4:")
for t in result:
    print(f"         {t}")
