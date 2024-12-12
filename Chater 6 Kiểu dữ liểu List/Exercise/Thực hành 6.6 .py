a = [ 
        [ 
            [3, 2], 
            [2, 7], 
            [1, 8] 
        ], 
        [ 
            [2, 9], 
            [5, 8], 
            [7, 20] 
        ] 
    ]   

# Bài toán 1: In ra tất cả các phần tử trong list theo thứ tự giảm dần và không có số trùng lặp
def flatten_and_sort(lst):
    """
    Hàm này nhận vào một list lồng nhau và trả về một list mới chứa tất cả các phần tử
    trong list ban đầu được sắp xếp theo thứ tự giảm dần và không có phần tử nào bị trùng lặp.
    """

    # Tạo một list rỗng để lưu trữ tất cả các phần tử trong list ban đầu
    flat_list = []

    # Duyệt qua từng phần tử trong list ban đầu
    for sublist1 in lst:
        for sublist2 in sublist1:
            for item in sublist2:
                # Nếu phần tử chưa tồn tại trong flat_list thì thêm phần tử đó vào flat_list
                if item not in flat_list:
                    flat_list.append(item)

    # Sắp xếp flat_list theo thứ tự giảm dần
    flat_list.sort(reverse=True)

    # Trả về flat_list
    return flat_list

# Bài toán 2: In ra các cặp số mà chúng chia hết được cho nhau
def find_divisible_pairs(lst):
    """
    Hàm này nhận vào một list lồng nhau và in ra tất cả các cặp số
    mà số thứ nhất chia hết cho số thứ hai.
    """
    for sublist1 in lst:
        for sublist2 in sublist1:
            for i in range(len(sublist2)):
                for j in range(i + 1, len(sublist2)):
                    if sublist2[i] % sublist2[j] == 0:
                        print(f"({sublist2[i]};{sublist2[j]})")
                    if sublist2[j] % sublist2[i] == 0:
                        print(f"({sublist2[j]};{sublist2[i]})")

# Bài toán 3: In ra các bộ 3 số khác nhau sao cho 1 số bằng tổng 2 số còn lại
def find_triplets(lst):
    """
    Hàm này nhận vào một list lồng nhau và in ra tất cả các bộ ba số khác nhau
    sao cho một số bằng tổng hai số còn lại.
    """
    for sublist1 in lst:
        for sublist2 in sublist1:
            for i in range(len(sublist2)):
                for j in range(i + 1, len(sublist2)):
                    for k in range(j + 1, len(sublist2)):
                        if sublist2[i] == sublist2[j] + sublist2[k]:
                            print(f"{sublist2[i]} = {sublist2[j]} + {sublist2[k]}")
                        if sublist2[j] == sublist2[i] + sublist2[k]:
                            print(f"{sublist2[j]} = {sublist2[i]} + {sublist2[k]}")
                        if sublist2[k] == sublist2[i] + sublist2[j]:
                            print(f"{sublist2[k]} = {sublist2[i]} + {sublist2[j]}")

# Gọi các hàm và in kết quả
print(f"Ket qua 1: {flatten_and_sort(a)}")
print("Ket qua 2:")
find_divisible_pairs(a)
print("Ket qua 3:")
find_triplets(a)