n = 5
print("\n14. Hollow Alphabet Pyramid")
for i in range(1, n+1):
    print(" " * (n-i), end="")
    for j in range(2*i-1):
        if j==0 or j==2*i-2 or i==n:
            print(chr(64+i), end="")
        else:
            print(" ", end="")
    print()