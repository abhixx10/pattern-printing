n = 10
print("\n9. Odd Pyramid")
for i in range(1, n+1):
    print(" " * (n-i), end="")
    num = 1
    for j in range(i):
        print(num, end=" ")
        num += 2
    print()