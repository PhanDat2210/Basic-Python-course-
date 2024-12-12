x = (True, 'Vu', 4, 9, 5, 25, 6.25, (1, 2), ['Vu', 'Coder'], False, (3, 'a'))
print('Cau 1:',[i for i in range(len(x)) if x[i]==i**2])
print('cau 2:',[tuple(x[i]) for i in range(len(x)) if type (x[i]) == list or type(x[i]) == tuple])

def count_data_types(x):
    # Tạo một từ điển để đếm số lần xuất hiện của mỗi kiểu dữ liệu
    type_count = {}

    for item in x:
         # Lấy kiểu dữ liệu của phần tử hiện tại
        data_type = type(item).__name__
        # Nếu kiểu dữ liệu đã tồn tại trong từ điển, tăng số đếm lên 1
        if data_type in type_count:
            type_count[data_type] += 1
            # Nếu kiểu dữ liệu chưa tồn tại trong từ điển, khởi tạo số đếm là 1
        else:
            type_count[data_type] = 1
    
    # Chuyển đổi từ điển thành danh sách các tuple
    result = [(key, value) for key, value in type_count.items()]
    
    return result
output = count_data_types(x)
print('Cau 3:',output)