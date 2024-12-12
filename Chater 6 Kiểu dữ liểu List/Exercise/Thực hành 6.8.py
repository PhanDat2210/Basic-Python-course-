def main():
    x = list(map(int, input("Nhập list x, cách nhau bằng dấu cách: ").split()))

    while True:
        print("\nChọn chức năng:")
        print("1. Tìm phần tử thuộc x nhưng không thuộc y")
        print("2. Kiểm tra xem x và y có giống nhau")
        print("3. Chia list x thành các list con có độ dài d")
        print("4. Tìm các cặp phần tử trong x có tổng bằng n")
        print("0. Thoát")

        choice = input("Nhập lựa chọn của bạn: ")

        if choice == '1':
            y = list(map(int, input("Nhập list y, cách nhau bằng dấu cách: ").split()))
            phan_tu_khac_nhau(x, y)
        elif choice == '2':
            y = list(map(int, input("Nhập list y, cách nhau bằng dấu cách: ").split()))
            kiem_tra_giong_nhau(x, y)
        elif choice == '3':
            d = int(input("Nhập độ dài d của list con: "))
            chia_list(x, d)
        elif choice == '4':
            n = int(input("Nhập số n: "))
            tim_cap_tong(x, n)
        elif choice == '0':
            break
        else:
            print("Lựa chọn không hợp lệ!")

def phan_tu_khac_nhau(x, y):
    """Tìm các phần tử thuộc x nhưng không thuộc y"""
    khac_nhau = list(set(x) - set(y))
    print(f"Các phần tử thuộc x nhưng không thuộc y: {khac_nhau}")

def kiem_tra_giong_nhau(x, y):
    """Kiểm tra xem x và y có giống nhau hay không"""
    if sorted(x) == sorted(y):
        print("Hai list giống nhau.")
    else:
        print("Hai list không giống nhau.")

def chia_list(x, d):
    """Chia list x thành các list con có độ dài d"""
    list_con = [x[i:i + d] for i in range(0, len(x), d)]
    print(f"Các list con của x: {list_con}")

def tim_cap_tong(x, n):
    """Tìm các cặp phần tử trong x có tổng bằng n"""
    cap_tong = []
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if x[i] + x[j] == n:
                cap_tong.append((x[i], x[j]))
    if cap_tong:
        print(f"Các cặp phần tử trong x có tổng bằng {n}: {cap_tong}")
    else:
        print(f"Không tìm thấy cặp phần tử nào có tổng bằng {n}")

if __name__ == "__main__":
    main()