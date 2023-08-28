def TernarySearch(arr: list[int], key: int) -> int:
    start = 0
    end = len(arr)
    count = 0
    while start <= end:
        count += 1
        mid = int((start + end)/2)
        if arr[mid] > key:
            end = mid - 1

        elif arr[mid] < key:
            start = mid + 1
        
        else:
            print("COUNT", count)
            return(mid)
            
    print("COUNT", count)
    return(-1)

print(TernarySearch([1, 4, 6, 7, 9, 12, 20], 6))