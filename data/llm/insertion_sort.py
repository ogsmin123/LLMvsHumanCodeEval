# Insertion sort implementation in Python
def insertion_sort(arr):
    # Traverse from the second element to the end of the array
    for i in range(1, len(arr)):
        key = arr[i]  # The element to be positioned
        j = i - 1

        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Place the key at its correct position
        arr[j + 1] = key

    # The array is sorted in place, no need to return it

# Example usage:
# arr = [12, 11, 13, 5, 6]
# insertion_sort(arr)
# print(arr)  # Output will be [5, 6, 11, 12, 13]