n = 5
print("\n38. AlphaNum Triangle")
for i in range(1, n+1):
    for j in range(i):
        print(chr(64+j+1) + str(j+1), end=" ")
    print()