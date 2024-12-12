n = int(input("Nhập n:"))
ten_nguoi1 = []
for i in range(n):
    ten_nguoi1.append(input(f"Nhap nguoi thu {i}:"))
max_ten = max(ten_nguoi1, key=len)
print("Ket qua 1:", max_ten)

avg_ten_nguoi_length = sum(len(t)for t in ten_nguoi1) / n
print("Ket qua 2:", avg_ten_nguoi_length)

ten_nguoi_formatted =[]
for t in ten_nguoi1:
    words = t.split()
    formatted_words =[word.capitalize() for word in words]
    ten_nguoi_formatted.append(" ".join(formatted_words))

print("Ket qua 3:", ' '.join(ten_nguoi_formatted))

ten_nguoi_sorted = sorted(ten_nguoi_formatted,key=lambda x: x.split()[-1].title())
print("Ket qua 4:", ' '.join(ten_nguoi_sorted))
