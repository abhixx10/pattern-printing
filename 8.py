for i in range(5, 0, -1):
    for j in range(i):
        if j==0 or j==i-1 or i==5:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()