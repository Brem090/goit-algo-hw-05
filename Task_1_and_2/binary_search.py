def binary_search(arr, value):
    left, right = 0, len(arr) - 1
    iterations = 0
    while left <= right:
        iterations += 1
        mid = left + (right - left) // 2

        if arr[mid] == value:
            return iterations, arr[mid]

        if arr[mid] < value:
            left = mid + 1
        else:
            right = mid - 1

    upper_bound = arr[left] if left < len(arr) else None
    return iterations, upper_bound

arr = [1.2, 2.3, 3.4, 4.5, 5.6, 6.7, 7.8, 8.9, 9.0, 10.1, 11.2, 12.3, 13.4, 14.5, 15.6]
value = 10.5
print(binary_search(arr, value))