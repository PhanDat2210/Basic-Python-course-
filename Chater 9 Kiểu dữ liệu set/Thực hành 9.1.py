user_input = input("Nhập dãy số")
n = set(int(x) for x in user_input.split())
print("Kết quả 1:",sum(n))
even_numbers = {x for x in n if x % 2 == 0}
odd_numbers = {x for x in n if x % 2 != 0}
print("Kết quả 2:",even_numbers,odd_numbers)
sorted_list = sorted(list(n),reverse=True)
print("Kết quả 3:",sorted_list)

b = True
for i in range(len(sorted_list) - 1):
    if sorted_list [i] +1 != sorted_list[i+1]:
        b = False
        break
print("Kết quả 4:",b)