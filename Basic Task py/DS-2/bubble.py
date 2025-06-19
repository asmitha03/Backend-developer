num = [2,6,55,45,23]
a = len(num)
for i in range(a):
    for j in range(a - 1 - i):
        if num[j] > num[j + 1]:
            temp = num[j]
            num[j] = num[j + 1]
            num[j + 1] = temp
print("sorted list:",num)