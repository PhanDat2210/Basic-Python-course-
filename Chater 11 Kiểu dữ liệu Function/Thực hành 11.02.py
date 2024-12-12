def program_1(x, y):

    if y == 0:
        print("Khong the thuc hien phep chia cho 0")
    else:
        return x / y


print("Ket qua 1:")
print(program_1(6, 2))
print(program_1(-7, 2))
print(program_1(8, 0))
print(program_1(-9, 3.5))
print(program_1(11, 4))

def program_2(f,*a1):
    result = f 
    for a2 in a1:
        if a2 == 0:
            print("Khong the thuc hien phep chia 0")
            return None
        result /= a2
    return result
print('\nKet qua 2:')
print(program_2(6, 2)) 
print(program_2(100, 2, 5))
print(program_2(1000, 2, 5, 4, 5))
print(program_2(1000, 2, 0, 4, 5))
print(program_2(1000))
