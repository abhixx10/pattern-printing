for i in range(1, 5+1):
    print(" " * (5-i), end="")
    for j in range(2*i-1):
        if j==0 or j==2*i-2 or i==5:
            print(chr(64+i), end="")
        else:
            print(" ", end="")
    print()