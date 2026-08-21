n = int(input("Enter a num -> "))
print("\n52. Alt * #")
for i in range(1, n+1):
    for j in range(i):
        if j%2==0:
            print("*", end=" ")
        else:
            print("#", end=" ")
    print()