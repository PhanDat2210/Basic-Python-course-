import math

# Nhập vào hai mệnh đề a và b
a = bool(input("Enter a (true/false): "))  # Sử dụng input dưới dạng bool
b = bool(input("Enter b (true/false): "))

# Thực hiện các phép toán logic
c = a and b
d = a or b
e = a and not b
f = (a and not b) or (not a and b)

# In kết quả dưới dạng True/False
print(f"c (a and b): {c}")
print(f"d (a or b): {d}")
print(f"e (a and not b): {e}")
print(f"f (only one of a or b is true): {f}")
