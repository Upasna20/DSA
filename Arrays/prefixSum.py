arr = [2, 4, 6, 8, 10]
subarray_sum = []
for lower_bound in range(len(arr)):
    sum = arr[lower_bound]
    for upper_bound in range(lower_bound + 1, len(arr)):
        sum += arr[upper_bound]
        subarray_sum.append(sum)
print(subarray_sum)
print(f'maximum from the subarray sum is: {max(subarray_sum)}')