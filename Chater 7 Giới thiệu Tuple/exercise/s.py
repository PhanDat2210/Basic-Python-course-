a = [3, 5.5, "ab", 2, "Vu", 0, 6, [2, 3, 4], False, [1, 2], True, 1.13]
temp1 = []

for item1 in a:
    if isinstance(item1, int):
        for item2 in a:
            if isinstance(item2, int) and item1 != bool and item1 != item2 and (item1, item2) not in temp1 and (item2, item1) not in temp1:
                temp1.append((item1, item2))
    elif isinstance(item1, bool):
        for item2 in a:
            if isinstance(item2, bool) and item1 != item2 and (item1, item2) not in temp1 and (item2, item1) not in temp1:
                temp1.append((item1, item2))

print("Kết quả 3:", tuple(temp1))