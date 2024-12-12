def program_1(*elements):
    return [element for element in elements if isinstance(element, (int, float))]
def program_2(*elements):
    return [element for element in elements if isinstance(element, str)]
def program_3(*elements):
    numeric_elements = [element for element in elements if isinstance(element, (int, float))]
    string_elements = [element for element in elements if isinstance(element, str)]
    return (sum(numeric_elements), ''.join(string_elements))
print('Ket qua 1:')
print(program_1(1, 'abc', 5, True, range(10), lambda x : x**2))  # Output: [1, 5]

print('\nKet qua 2:')
print(program_2('Vu', 2, False, 'Coder', enumerate([1,2,3]), 'Python'))  # Output: ['Vu', 'Coder', 'Python']

print('\nKet qua 3:')
print(program_3(1, 2, '3', 4, '5', 6, 7, '8', '9', '10', {11, 12, 13}, False))  # Output: (28, '3859610710910')
print(program_3('1', 2, '3', '4', '5', 6, [7, 8], '9', 10, {11, 12, 13}))  # Output: (24, '1234567910')