for i in range(1, 5+1):
    print(" " * (5-i), end="")
    for j in range(1, i+1):
        print(chr(64+j), end="")
    for j in range(i-1, 0, -1):
        print(chr(64+j), end="")
    print()