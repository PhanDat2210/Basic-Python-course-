def program_1(x, y, z):
    return max(x, y, z)

print('Ket qua 1:')
print(program_1(19, 13, 12))
print(program_1(12, 16, 11))
print(program_1(3, 1, 4))

def program_2(*a):
    return max(a)
print('Ket qua 2:')
print(program_2(19, 13, 12))
print(program_2(12, 16))
print(program_2(3, 1, 4, 5, 10, 3, 2, -1))