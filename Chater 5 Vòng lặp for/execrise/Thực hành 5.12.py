n = 10
for i in range(1, n + 1):
    for j in range(n, 0, -1):
        if j >= i + 1:
            print("  ", sep="", end="")
        else:
            print("0 ", sep="", end="")
    for k in range(n + 1, 2 * n + 2):
        if k <= n + i - 1:
            print("0 ", sep="", end="")
        else:
            print(" ", sep="", end="")
    print()


print()
