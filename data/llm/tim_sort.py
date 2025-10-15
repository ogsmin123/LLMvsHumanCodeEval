def insertion_sort(arr, left, right):
    # Perform insertion sort on the subarray from left to right.
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        # Shift elements of the sorted segment to find the correct position for the key.
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge(arr, left, mid, right):
    # Merge two sorted subarrays into a single sorted subarray.
    len1, len2 = mid - left + 1, right - mid
    left_part, right_part = arr[left:mid + 1], arr[mid + 1:right + 1]

    i, j, k = 0, 0, left
    # Merge the two parts by comparing elements.
    while i < len1 and j < len2:
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    # Copy any remaining elements of left_part, if any.
    while i < len1:
        arr[k] = left_part[i]
        i += 1
        k += 1

    # Copy any remaining elements of right_part, if any.
    while j < len2:
        arr[k] = right_part[j]
        j += 1
        k += 1

def tim_sort(arr):
    # Define the minimum run size for the TimSort algorithm.
    MIN_RUN = 32
    n = len(arr)

    # Sort individual subarrays of size MIN_RUN using insertion sort.
    for start in range(0, n, MIN_RUN):
        end = min(start + MIN_RUN - 1, n - 1)
        insertion_sort(arr, start, end)

    # Start merging from size MIN_RUN. Double the size each iteration.
    size = MIN_RUN
    while size < n:
        # Pick starting point of left subarray. Merge arr[left..left+size-1] and arr[left+size..left+2*size-1]
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            # Merge subarrays arr[left...mid] & arr[mid+1...right]
            if mid < right:
                merge(arr, left, mid, right)

        size *= 2

# Example usage:
# arr = [5, 21, 7, 23, 19]
# tim_sort(arr)
# print(arr)  # Output will be a sorted array
```

This implementation of TimSort uses a combination of insertion sort and merge sort. The `MIN_RUN` constant defines the size of subarrays that will be sorted using insertion sort, which is efficient for small arrays. The merge function combines sorted subarrays into larger sorted subarrays. The algorithm progressively merges larger subarrays until the entire array is sorted. This approach leverages the strengths of both insertion sort (for small arrays) and merge sort (for larger arrays), making it efficient for a wide range of input sizes and distributions.