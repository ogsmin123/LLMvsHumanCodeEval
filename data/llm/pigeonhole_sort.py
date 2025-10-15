def pigeonhole_sort(arr):
    # Find the minimum and maximum values to determine the range of pigeonholes needed
    min_val = min(arr)
    max_val = max(arr)
    size = max_val - min_val + 1  # Calculate the size of the range

    # Initialize pigeonholes
    holes = [0] * size

    # Populate the pigeonholes
    for number in arr:
        holes[number - min_val] += 1

    # Reconstruct the sorted array from the pigeonholes
    index = 0
    for i in range(size):
        while holes[i] > 0:
            arr[index] = i + min_val
            index += 1
            holes[i] -= 1

# Example usage:
# arr = [8, 3, 2, 7, 4, 6, 8]
# pigeonhole_sort(arr)
# print(arr)  # Output will be a sorted array: [2, 3, 4, 6, 7, 8, 8]