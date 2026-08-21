num = 1
for i in range(1, 5+1):
    print(" " * (5-i), end="")
    temp = []
    for j in range(i):
        temp.append(str(num))
        num += 1
    print("".join(temp) + "".join(temp[-2::-1]))