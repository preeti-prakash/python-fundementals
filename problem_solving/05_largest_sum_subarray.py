def largest_sum_subarray(arr):
    if len(arr) == 0:
        return 0

    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum+num, num)
        max_sum = max(max_sum, current_sum)

    return max_sum


print(largest_sum_subarray([1, 2, -1, 3, 4, 10, 10, -10, -1]))
print(largest_sum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
