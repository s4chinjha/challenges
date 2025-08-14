def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

nums = [64, 44, 25, 12, 24, 13]
print("Original Numbers = ", nums)
sorted_nums = bubble_sort(nums)
print("Sorted NUmbers = ", sorted_nums)
