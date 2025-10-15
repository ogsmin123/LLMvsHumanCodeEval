# Stooge Sort Implementation in Python

def stooge_sort(arr, l, h):
    # Base case: If there is only one element, do nothing
    if l >= h:
        return

    # If the first element is smaller than the last, swap them
    if arr[l] < arr[h]:
        arr[l], arr[h] = arr[h], arr[l]

    # If there are more than two elements in the array
    if h - l + 1 > 2:
        # Calculate the third of the current segment
        t = (h - l + 1) // 3

        # Recursively sort the first 2/3 of the array
        stooge_sort(arr, l, h - t)

        # Recursively sort the last 2/3 of the array
        stooge_sort(arr, l + t, h)

        # Recursively sort the first 2/3 of the array again
        stooge_sort(arr, l, h - t)

# Example usage:
# arr = [2, 4, 5, 3, 1]
# stooge_sort(arr, 0, len(arr) - 1)
# print(arr)  # Output should be a sorted array [1, 2, 3, 4, 5]