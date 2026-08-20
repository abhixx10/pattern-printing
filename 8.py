n = 5
print("\n8. Hollow Decreasing")
for i in range(n, 0, -1):
    for j in range(i):
        if j==0 or j==i-1 or i==n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()