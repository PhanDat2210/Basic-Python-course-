# Lý thuyết 06.E - Các phép toán duyệt list (interation)

x = [1, 2, 3, "abc", True]

# range là 1 kiểu dữ liệu thuộc dạng iterable
# print(6 in x)
# for i in range (len(x)):
# print(x[i])
#  print(f"x[{i}] = {x[i]}")
print(x)

# for i in x:
#   print(i)
i = 0
# while i < len(x):
#  print(x[i])
# i += 1

# for i in x :
#  print(i)

for i in range (len(x)):
    x[i] *= 2
    #print(i)

print(x)