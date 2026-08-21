n = 3
print("\n36. Alpha + Number")
for i in range(1, n+1):
    print(" " * (n-i), end="")
    print(chr(64+i) + str(i) + chr(64+i))