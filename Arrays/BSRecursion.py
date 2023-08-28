arr = [2, 4, 6, 8, 10]
key = 10
def bsRecursion(start=0, end=len(arr) - 1, arr=arr, key=key ):
    mid = int((start + end) / 2)
    if start > end:
        return -1
    if arr[mid] == key:
        return mid
    if arr[mid] < key:
        start = mid + 1
        return bsRecursion(start, end)
    if arr[mid] > key:
        end = mid - 1
        return bsRecursion(start, end)

print(bsRecursion())
