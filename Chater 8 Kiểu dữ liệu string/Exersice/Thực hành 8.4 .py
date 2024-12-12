s = 'Vu Nguyen Coder Vu Coder lap trinh Pyhon'
 #1  . đếm số từ đơn
words = s.split()
so_tu_don = len(words)
print(f"Kết quả 1:{so_tu_don}")
# 2. List tần suất các từ
word_count = {}  # Tạo từ điển rỗng để chứa tần suất từ
for word in words:
    if word in word_count:
        word_count[word] += 1  # Nếu từ đã có trong từ điển, tăng tần suất lên 1
    else:
        word_count[word] = 1  # Nếu từ chưa có trong từ điển, thêm nó và đặt tần suất là 1
tan_suat_tu = list(word_count.items())  # Chuyển từ điển thành danh sách các tuple
print(f"Kết quả 2:{tan_suat_tu}")
# 3. Chuỗi bọc dấu sao
star_line = "*" * (len(s) + 4)  # Hàng sao trên và dưới
star_string = f"*{' * '.join(['*' + word + '*' for word in words])} *"
print(f"Ket qua 3:\n{star_line}\n{star_string}\n{star_line}")

# 4. Chuỗi đảo ngược từ
reversed_words = " ".join([word[::-1] for word in words])
print(f"Ket qua 4: {reversed_words}")

"""Nhập một chuỗi s gồm các từ đơn. (từ đơn là 1 chuỗi kí tự con ko có khoảng trắng)
1 - Đếm số từ đơn có trong câu
2 - In ra list liệt kê tần suất của các từ trong chuỗi s. Các phần tử trong list là một tuple gồm từ và giá trị tần suất. 
3 - In ra một chuỗi mới bọc chuỗi cũ trong các dấu sao, phía trên, dưới, trái, phải và ở các khoảng trắng đều cần có 1 dấu sao (*)
4 - In ra chuỗi mới với các phần tử là các từ bị đảo ngược trong chuỗi s`"""