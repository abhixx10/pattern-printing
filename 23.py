n = 4
print("\n23. Consecutive Palindromic")
num = 1
for i in range(1, n+1):
    print(" " * (n-i), end="")
    temp = []
    for j in range(i):
        temp.append(str(num))
        num += 1
    print("".join(temp) + "".join(temp[-2::-1]))