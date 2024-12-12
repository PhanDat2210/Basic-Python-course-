# Lý thuyết 06.C - Các phép toán sửa đổi list

# Khi nhắc đến sửa đổi (update/change) một list,
# chúng ta sẽ quan tâm đến việc thay đổi dữ liệu, thêm phần tử,
# xoá phần tử, thay đổi thứ tự,...

x = [1, 2, 3, 5, "abc", True]
# x+=[4,5,6]
# x.append(4)
# x.extend([4,5,6])
# x[0:3] = [4,5,6]
# slicing
# x.append([4,5,6])

# y = x + [4, 5, 6]
# concatenate :phép nối

# x.insert(1,10) chèn
#del x[3:5] # xoá phần tử trong xóa [1, 2, 3, True]
#x.clear() # xoá phần tử trong xồng [1, 2, 3, 5, 'abc', True]
#x.reverse() # dao nguoc [True, 'abc', 5, 3, 2, 1]
print(x)
