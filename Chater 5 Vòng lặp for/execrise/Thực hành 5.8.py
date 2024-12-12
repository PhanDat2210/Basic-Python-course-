def main():
    n = int(input("Nhập n: "))

    # Kiểm tra n dương
    if n <= 0:
        print("Vui lòng nhập số nguyên dương.")
        return

    # Khởi tạo các biến
    temp = n
    count = 0
    sum_digits = 0
    reverse = 0

    # Tính số chữ số, tổng các chữ số và đảo ngược số
    while temp > 0:
        digit = temp % 10  # Lấy chữ số cuối
        sum_digits += digit  # Tính tổng các chữ số
        reverse = reverse * 10 + digit  # Đảo ngược số
        temp //= 10  # Bỏ chữ số cuối
        count += 1  # Đếm số chữ số

    # In ra kết quả
    print(f"Ket qua 1: {reverse}")
    print(f"Ket qua 2: So n co {count} chu so")
    print(f"Ket qua 3: {sum_digits}")

    # Nhập vị trí muốn lấy
    position = int(input("Nhập vị trí muốn lấy: "))

    # Kiểm tra vị trí
    if position < 1 or position > count:
        print("Ko ton tai vi tri nay")
    else:
        # Lấy chữ số tại vị trí yêu cầu
        temp = n
        digits = []  # Danh sách chứa các chữ số
        while temp > 0:
            digits.append(temp % 10)  # Lấy chữ số cuối và thêm vào danh sách
            temp //= 10  # Bỏ chữ số cuối
        digits.reverse()  # Đảo ngược danh sách để có thứ tự từ trái sang phải

        # In chữ số tại vị trí yêu cầu
        print(f"Ket qua 4: {digits[position - 1]}")  # Vị trí bắt đầu từ 0

if __name__ == "__main__":
    main()

