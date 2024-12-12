n = int(input("Nhap n:"))
print("Ket qua 1:", end=" ")
for i in range(1, n, 2):
    print(i, end=" ")
print("\nKet qua 2:", end=" ")
for a in range(1, n):
    if a % 3 == 0:
        print(a, end=" ")
print("\nKet qua 3:", end=" ")
for g in range(1, n + 1):
    if g % 2 != 0 and g % 3 == 0:
        print(g, end=" ")
print("\nKet qua 4:", end=" ")
for j in range(-n, n + 1):
    if j % 5 == 0:
        print(j, end=" ")
