n = 9
print("\n11. Row Number Pyramid")
for i in range(1, n+1):
    print(" " * (n-i), end="")
    for j in range(i):
        print(i, end=" ")
    print()