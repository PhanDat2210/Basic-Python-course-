import math

x = float(input("Enter x: "))
y = float(input("Enter y: "))

# Tính toán các biểu thức
result1 = x * y + x / y
result2 = x + 1 / (x + 1 / (x + 1 / (x + y)))
result3 = math.sqrt(pow(3 * x + 2 * y, 2) * pow(5 * x + 1, 3))

# Làm tròn đến hai chữ số thập phân
def format_to_two_decimal(num):
    return f"{num:.2f}"

print("1)", format_to_two_decimal(result1))
print("2)", format_to_two_decimal(result2))
print("3)", format_to_two_decimal(result3))
