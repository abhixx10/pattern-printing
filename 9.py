for i in range(1, 5+1):
    print(" " * (5-i), end="")
    num = 1
    for j in range(i):
        print(num, end=" ")
        num += 2
    print()