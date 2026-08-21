n = 4
print("\n44. Digit Diamond")
for i in range(1, n+1):
    print(" " * (n-i) + str(n) * (2*i-1))
for i in range(n-1, 0, -1):
    print(" " * (n-i) + str(n) * (2*i-1))