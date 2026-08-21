n = 3
print("\n39. 1-0 Pattern")
for i in range(1, n+1):
    for j in range(i):
        print((i+j+1) % 2, end=" ")
    print()