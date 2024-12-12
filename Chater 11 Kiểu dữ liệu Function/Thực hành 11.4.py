def program_1(*x):
    return [i for i in x if i % 2 == 0]


def program_2(*x):
    return [i for i in x if i % 2 != 0]


def program_3(*x):
    return [i for i in x if i > 0]

def program_4(*numbers):
    return [num for num in numbers if num < 0]

def program_5(*numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    return [num for num in numbers if is_prime(num)]

def program_6(numbers, *filters):
    result = numbers
    for filter_func in filters:
        result = filter_func(*result)
    return sorted(result)

print("Ket qua 1: ", end="")
print(program_1(3, 4, 1, 9, 10, 8, 20))

print("Ket qua 2: ", end="")
print(program_2(15, 3, 6, 9, 7))

print("Ket qua 3: ", end="")
print(program_3(8, 10, 5, 6, 3, 9, 2, 7, 14))

print('Ket qua 4: ', end = '')
print(program_4(-9, 3.5))

print('Ket qua 5: ', end = '')
print(program_5(11, 4, 9, 13, 6, 8, -23, 12, 1))

print('Ket qua 6: ')
print('\t', program_6([7, 2, 6 , 4, 8, 13], program_1))
print('\t', program_6([-7, 2, 6 , 4, 11, -13, 29, 1], program_3, program_5))
print('\t', program_6([-3, -2, -1 ,0 , 1, 2, 3], program_3, program_4))