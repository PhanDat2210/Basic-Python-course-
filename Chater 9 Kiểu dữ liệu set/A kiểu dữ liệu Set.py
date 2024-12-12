x = [
    1,
    2,
    2,
    3,
    4,
    3,
    2,
]  # x[0] = 1, x[1] = 2, x[2] = 2, x[3] = 3, x[4] = 4, x[5] = 3, x[6] = 2

y = {1, 2, 2, 2, 3, 4, 5}
a = set()
print(x)  # [1, 2, 2, 3, 4, 3, 2]
print(y)  # {1, 2, 3, 4, 5}
print(type(a))
print(sorted(y))  # tạo ra 1 list và sắp xếp chỉ numbers

print([element for element in enumerate(y)])

# kiểm tra sự tồn tại trong 1 nhóm(membership test operator)

print(1 in a)  # trả logic

y.add(6)
y.update(["def", "ghi", "jkl", "mno"])
y.discard(2)
y.remove('jkl')
print(y)
