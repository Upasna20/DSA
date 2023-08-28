# arr = [2, 4, 6, 8, 10]
# for i in range(0, len(arr)):
#     for j in range(i+1, len(arr)):
#         print("(", end="")
#         for h in range(i, j+1):
#             print(arr[h], end=",")
#         print("), ", end=" ")
#     print()
    
# max sum using brute force
arr = [10, 8, 20, 23]
max_sum = 0
for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        count = 0
        print("(", end="")
        for h in range(i, j+1):
            count += arr[h]
            print(arr[h], end=",")
        print("), ", end=" ")
        if max_sum < count:
            max_sum = count
    print()
print(max_sum)
