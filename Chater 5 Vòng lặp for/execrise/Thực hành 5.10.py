for i in range(10):
    if i % 2 == 0:
        for j in range(10):
            print(j, end=" ")
    else:
        for j in range(9, -1, -1):
            print(j, end=" ")
    print()
print("\n")
for b in range(10):
    for v in range(10):
        if b == 0 or b == 9 or v == 0 or v == 9:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()
print("\n")
for c in range(10):
    for d in range(10):
        if c == d:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()
print("\n")
for e in range(10):
    for h in range(10):
        if e == h or e + h == 9:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()
print("\n")
for e in range(10):
    for h in range(10):
        if (e + h) % 2 == 0:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()
print("\n")
# Kích thước hình vuông
#6. Hình vuông thập phân đường chéo 0

for i1 in range(10):
    for j1 in range(10):
        if i1 == j1 :
            print(0, end=" ")
        else:
            print((j1 + i1) % 10,end=" ") 
    print()