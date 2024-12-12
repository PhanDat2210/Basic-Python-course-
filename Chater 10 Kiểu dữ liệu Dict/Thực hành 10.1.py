d = {"ad":12,
     "cd":5.2,
     "ef":100,
     "gh":"ab",
     "ik":False,
     "mno":[1,2,3],
     "pq":"ab",
     "xyz":"Vu Nguyen",
     "www":"coder",
     }
s = input("Enter a string: ")

is_key = s in d
print(f"Kết quả 1: {is_key}")

# Bước 2: In ra tất cả các key mà có value tương ứng là s
keys_with_value_s = [k for k, v in d.items() if v == s]
print(f"Kết quat 2: '{s}': {keys_with_value_s}")

# Bước 3: In ra list gồm các value là chuỗi trong dict
string_values =[v for v in d.values() if isinstance(v, str)]
print(f"Kết quả 3: {string_values}")

# Bước 4: In ra set gồm các value là số trong dict
numeric_values = {v for v in d.values() if isinstance(v, (int, float))}
print(f"Kêt quả 4: {numeric_values}")

