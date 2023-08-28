arr = [-2,-3, 4, -1, -2, 1, 5, -3]
def Kadane(arr: list[int]) -> int:
    currSum = 0
    maxSum = 0
    for element in arr:
        if currSum < 0:
            currSum = 0
        currSum += element
        if maxSum < currSum:
            maxSum = currSum

    return maxSum

print(Kadane(arr))