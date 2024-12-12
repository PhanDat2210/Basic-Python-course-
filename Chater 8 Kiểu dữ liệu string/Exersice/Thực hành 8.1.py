s = "abc d2e3 faaXYZ"
print("Kết qua 1:", s.upper())
print("Kết quả 2:", s.count(" "))
alphabe_count , digit_count = sum(item.isalpha() for item in s), sum(item.isdigit() for item in s)
print("Kết quả 3:", alphabe_count,"&",digit_count)

def find_longest_word(p):
    s_reading = "abc d2e3 faaXYZ"  # assuming this is the input string
    for key, value in p.items():
        s_reading = s_reading.replace(key, value)
    return s_reading

p = {'1': 'mot', '2': 'hai', '3': 'ba'}
print("Kết quả 4:",find_longest_word(p))  # Output: abc dhaiemotba faaXYZ
char_frequency = {}
for c in s:
    if c.isalpha():
        if c.lower() in char_frequency:
            if c.isupper():
                #c.isupper(): Kiểm tra xem ký tự c có phải là chữ hoa không
                char_frequency[c.lower()][1] += 1
                #Nếu đúng, tăng giá trị đếm chữ hoa (char_frequency[c.lower()][1]) lên 1.
            else:
                char_frequency[c.lower()][0] += 1
        else:
            if c.isupper():
                char_frequency[c.lower()] = [0, 1]
            else:
                char_frequency[c.lower()] = [1, 0]

for k, v in char_frequency.items():
    if v[0] > 0:
        print(f"({k} - {v[0]})", end=', ')
    if v[1] > 0:
        print(f"({k.upper()} - {v[1]})", end=', ')