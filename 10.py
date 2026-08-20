n = 5
print("\n10. Same Number Pyramid")
for i in range(1, n+1):
    print(" " * (n-i), end="")
    print((str(i) + " ") * i)