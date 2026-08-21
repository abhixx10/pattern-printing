n = 5
print("\n34. Alphabet Pyramid")
for i in range(1, n+1):
    print(" " * (n-i), end="")
    for j in range(i):
        print(chr(64+j+1), end=" ")
    print()