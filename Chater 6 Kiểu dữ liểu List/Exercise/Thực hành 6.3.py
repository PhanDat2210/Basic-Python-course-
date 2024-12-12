n = [0, True, "Vu Nguyen", True, 15, 1.12, 20, 100, 2.2, 20, 100, 15]
y = [item for item in n if type(item) == int or type(item) == float]
print(f"Kết quả 1:{y}")

new_list = list(set(n))
print(f"Kết quả 2:{new_list}")

# 3. Tìm ra độ dài của list con dài nhất có các phần tử liên tiếp có cùng kiểu
max_length = 0
current_length =1
for i  in range (1,len(n)):
    if isinstance(n[i],type(n[i-1])):
        current_length += 1
    else:
        max_length = max(max_length, current_length)
        current_length = 1

max_length = max(max_length, current_length)

print(f"Kết quả 3:{max_length}")