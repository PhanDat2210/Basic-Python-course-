# phép toán hợp
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}


print(a | b)  # hoặc
print(a.union(b))
print(a & b)  # giao
print(a.intersection(b))
print(a - b)  # hiệu
print(a.difference(b))  # hiệu

# phép hiệu đói xứng (symetric difference)
print(a ^ b) # phép hiệu đói xứng a ^ b = a \b | b \a
print(a.symmetric_difference(b))

