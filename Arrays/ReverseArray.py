arr = [12, 33, 4, 5, 66, 7]
def ReverseArray(arr: list[int]) -> list[int]:
    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

print("Original Array: ", arr)
print("Reversed Array:", ReverseArray(arr))