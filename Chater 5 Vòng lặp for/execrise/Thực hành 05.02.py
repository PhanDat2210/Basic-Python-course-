import math
# điều kiện n > 1
def P(n):
    total = 0
    if n > 1:
        n = int(n)
        for i in range(1, n + 1):
            total += i
        return total
    else:
        print("Vailed ,please Enter Esc")


print("P(6) =", P(6))

m = int(input("Nhập m:"))

# Kiểm tra điều kiện m > 1
if m > 1:
    total = 0  # Biến tính tổng
    product = 1  # Biến tính tích (khởi tạo là 1 vì tích với 0 sẽ luôn bằng 0)
    product1 = 1
    product3 =0
    product4 = 0
    product5 = 0
    
    # Tính và in tổng
    print("P(", m, ") =", end="")
    for j in range(1, m + 1):
        total += j  # Cộng dồn giá trị vào tổng

        # In ra các số và dấu cộng cho tổng
        if j < m:
            print(j, end="+")
        else:
            print(j, end=" ")  # Số cuối không có dấu cộng

    print("=", total)  # In tổng

    # Tính và in tích
    print("Q(", m, ") =", end="")
    for j in range(1, m + 1):
        product *= j  # Nhân dồn giá trị vào tích

        # In ra các số và dấu nhân cho tích
        if j < m:
            print(j, end="*")
        else:
            print(j, end=" ")  # Số cuối không có dấu nhân

    print(" =", product)  # In tích
    print("R(", m, ") =", end="")
    for k in range(1, m + 1):
        if k % 2 != 0:
            product1 += k
            if k < m - 1:
                print(k, end="+")
            else:
                print(k, end=" ")
    print("=", product1)
    print("S(",m,") = ",end="")
    for h in range (0,m):
        h+=1
        product3 +=int(math.pow(h,3))
        if h < m :
            print(h,"^3 + ",end = "")
        else:
            print(h,"^3 = ",end = "")
    print(product3,end='\n')
    print("T(",m,") = ",end="")
    for b in range (0,m):
        b+=1
        if b <m:
            print(b,"/",b,"^",b," + ",end = "")
        else:
            print(b,"/",b,"^",b," = ",end = "")
        product4 +=b/(int(math.pow(b,b)))
    print("=",product4,end='\n')
    print("U(",m,") = ",end="")
    for c in range(0,m):
        c+=1 
        product5 +=c*(c+1)
        if c < m :
            print(c,"*",c+1," + ",end = "")
        else:
            print(c,"*",c+1," = ",end = "")
    print(product5,end='\n') 
    product6 = 0
    print("V(",m,") = ",end="")
# Vòng lặp để tạo và tính tổng của các số như 1, 11, 111, ...
    for ad in range(1, m + 1):  # ad chạy từ 1 đến m
        num = int('1' * ad)  # Tạo ra số như 1, 11, 111, ...
        product6 += num  # Cộng dồn giá trị vào product6
        if ad < m:
            print(f"{num} + ", end="")  # In số và dấu cộng
        else:
            print(f"{num} = ", end="")  # Số cuối cùng, in dấu bằng
# In tổng cuối cùng
    print(product6)
    print("X(",m,") = ",end="")
    product7 = 0
    total=0
    for he in range(1,m+1):
        product7 += sum (range(0,he+1))
        if he < m:
            print(f"({'+'.join(map(str,range(1,he+1)))}) +", end=" ")
        else:
            print(f"({'+'.join(map(str,range(1,he+1)))})", end=" ")
    print("=",product7,end ='')  
else:
    print("Invalid, không thỏa điều kiện")
    
