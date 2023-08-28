arr = [12, 3, 4, 55, 6]
count = 0
for i in range(0, len(arr) - 2):
    for j in range(i + 1, len(arr)):
        count += 1
        print((arr[i], arr[j]), end =" ")
    print()
print(count)
