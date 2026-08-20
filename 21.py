n = 5
print("\n21. Inverted Decreasing Width")
for i in range(n, 0, -1):
    print(" " * (n-i) + "* " * (2*i-1))