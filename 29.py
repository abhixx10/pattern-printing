n = 3
print("\n29. Hollow Cross")
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i==j or i+j==n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()