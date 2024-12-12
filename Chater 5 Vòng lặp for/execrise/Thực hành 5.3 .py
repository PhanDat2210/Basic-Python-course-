import math


def dem(n):

    print("Ket qua 1: ", end="")
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")
            count += 1
    print(f"\nKet qua 2: {count}")
    return count


def la_count(n):
    if n < 2:
        return False
    for j in range(2, int(math.sqrt(n) + 1)):
        if n % j == 0:
            return False
    return True


n = int(input("nhap n: "))
if dem(n):
    print("Ket qua 3: La so nguyen to")
else:
    print("Ket qua 3: Khong la so nguyen to")
