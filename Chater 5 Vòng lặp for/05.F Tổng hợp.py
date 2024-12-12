n = 5

for i in range(n):
    # if i == 0 :
    # continue
    for j in range(i+1 ):
            if j == 0 or j == i or i == n - 1:
                print("* ", end="")
    print()
