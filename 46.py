n = 3
print("\n46. Digit Diamond")
for i in range(1, n+1):
    print(" " * (n-i) + str(i) * i)
for i in range(n-1, 0, -1):
    print(" " * (n-i) + str(i) * i)