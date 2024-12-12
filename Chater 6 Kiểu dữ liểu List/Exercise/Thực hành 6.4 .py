def find_common_elemets(a, b):
    """Tìm các phần tử giống nhau giữa 2 list a1 và a2."""
    i = []
    for j in a:
        if j in b and j not in i:
            i.append(j)
    return i


def list_elemets(a, b):
    "" "Trộn 2 list a1 và a2, sắp xếp tăng dần, loại bỏ phần tử trùng lặp." ""
    i1 = a + b
    i1.sort()
    i2 = []
    for j1 in i1:
        if j1 not in i2:
            i2.append(j1)
    return i2


a = [5, 9, 12, 3, 7, 11, 2]
b = [8, 2, 0, 13, 7, 6, 9]
i = find_common_elemets(a, b)
j = list_elemets(a, b)
print("Kết quả 1:", i)
print("Kết quả 2:", j)
