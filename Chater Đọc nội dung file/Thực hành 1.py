class Person:
    def __init__(self, name, age, height, weight, region):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.region = region

    def __str__(self): 
        """Trả về chuỗi đại diện cho đối tượng Person."""
        return f'{self.name}, {self.age}, {self.height}, {self.weight}, {self.region}'
def program_load(file_name):
    """
    Đọc dữ liệu từ file và trả về danh sách các đối tượng Person.

    Args:
        file_name (str): Tên của file chứa dữ liệu.

    Returns:
        list: Danh sách các đối tượng Person.
    """
    person_list = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                # Tách thông tin từ dòng
                info = line.strip().split('|')
                # Tạo đối tượng Person
                person = Person(info[0], int(info[1]), float(info[2]), float(info[3]), info[4])
                person_list.append(person)
    except FileNotFoundError:
        print(f"File {file_name} không tồn tại.")
    return person_list
def program_add(file_name, person):
    """
    Thêm thông tin của một nhân vật vào file dữ liệu.

    Args:
        file_name (str): Tên của file chứa dữ liệu.
        person (Person): Đối tượng Person cần thêm.
    """
    try:
        with open(file_name, 'a') as file:
            file.write(person.__str__() + '\n')
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
print('Kết quả 1: ')
person_list = program_load('Chater Đọc nội dung file\Data.txt')
for person in person_list: 
    print(person.name, person.age, person.height, person.weight, person.region)

print('\nKết quả 2:')
program_add('Data.txt', Person('Yen', 25, 1.65, 60, 'Viet Nam'))
person_list = program_load('Chater Đọc nội dung file\Data.txt')
for person in person_list: 
    print(person.name, person.age, person.height, person.weight, person.region)