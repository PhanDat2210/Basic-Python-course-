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

# import math

# a,b = map (float,input ("nhap a,b:").split(","))
# c = (a*b) + (a/b)
# result = math.floor (c*100)/100 # 0 làm tròn 6.66
# print (f"answer: {result}")
# import math

# a,b = map (float,input ("nhap a,b:").split(","))
# c = (a*b) + (a/b)
# print (f"answer: {round(c,2)}") # làm tròn 6.67
# import math

# x,y = map (float,input("Enter x ,y :").split(","))
# z = math.sqrt(math.pow(3*x+2*y,2)*math.pow(5*x+1,3))
# print (f"Answer z: {round(z,2)}")
