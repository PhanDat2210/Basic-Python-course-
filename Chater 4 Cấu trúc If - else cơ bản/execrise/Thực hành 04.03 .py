# Nhập vào tháng của 1 năm. Cho biết tháng thuộc quý mấy trong năm và in ra màn hình. Nếu số tháng ko hợp lệ, in ra thông báo lỗi

month = int(input("Enter month :"))

ReturnValue1 = (f"Ket qua : Ko co thang {month}", "Ket qua : Quy 1")[
    month >= 1 and month <= 3
]
ReturnValue2 = (f"Ket qua : Ko co thang {month}", "Ket qua : Quy 2")[
    month >= 4 and month <= 6
]
ReturnValue3 = (f"Ket qua : Ko co thang {month}", "Ket qua : Quy 3")[
    month >= 7 and month <= 9
]
ReturnValue4 = (f"Ket qua : Ko co thang {month}", "Ket qua : Quy 4")[
    month >= 10 and month <= 12
]


print(ReturnValue1, ReturnValue2, ReturnValue3, ReturnValue4)

#CÁCH 2:
# Nhập vào tháng của năm từ người dùng
month = int(input("Enter month: "))

# Xác định quý của tháng hoặc thông báo lỗi nếu tháng không hợp lệ
if 1 <= month <= 3:
    result = "Ket qua : Quy 1"
elif 4 <= month <= 6:
    result = "Ket qua : Quy 2"
elif 7 <= month <= 9:
    result = "Ket qua : Quy 3"
elif 10 <= month <= 12:
    result = "Ket qua : Quy 4"
else:
    result = f"Ket qua : Ko co thang {month}"
    print(result)
    exit()

# Hiển thị các tùy chọn quý
print("Chon quy de in ket qua:")
print("1. Quy 1")
print("2. Quy 2")
print("3. Quy 3")
print("4. Quy 4")

# Nhập lựa chọn của người dùng
choice = int(input("Enter your choice (1-4): "))

# In kết quả dựa trên lựa chọn của người dùng
if choice == 1 and "Quy 1" in result:
    print("Ket qua : Quy 1")
elif choice == 2 and "Quy 2" in result:
    print("Ket qua : Quy 2")
elif choice == 3 and "Quy 3" in result:
    print("Ket qua : Quy 3")
elif choice == 4 and "Quy 4" in result:
    print("Ket qua : Quy 4")
else:
    print("Lựa chọn không hợp lệ hoặc quý không khớp với tháng.")


