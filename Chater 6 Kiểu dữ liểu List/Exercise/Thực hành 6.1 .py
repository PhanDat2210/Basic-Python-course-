n = [5, 9, 12, 3, 7, 11, 2]
n.reverse()
print("Ket qua 1:", end=" ")
for i in n:
    print(f"{i}", end=" ")

# i = n[0]
# j = n[6]
# x=i+j
# cách 2:
x = n.pop(0) + n.pop()
# pop(0) lấy phần tử đầu, pop() lấy phần tử cuối
print(f"\nKet qua 2: {x}")

if len(n) % 2 == 1:
    # Nếu độ dài danh sách là lẻ, lấy phần tử chính giữa
    mid_index = len(n) // 2
else:
    # Nếu độ dài danh sách là chan, lấy phần tử chính giữa
    mid_index = len(n) // 2 - 1
mid = n[mid_index]
print(f"Ket qua 3: {mid}")

tong_le =sum([item for item in n if item % 2 == 1])
tong_chan=sum([item for item in n if item % 2 == 0])
tich = tong_le * tong_chan

print(f"Ket qua 4: {tich}")
