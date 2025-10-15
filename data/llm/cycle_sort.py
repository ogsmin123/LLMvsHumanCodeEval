# Cycle sort is an in-place, unstable sorting algorithm that minimizes the number of writes to the array.
# It is optimal for situations where write operations are costly.

def cycle_sort(arr):
    # Loop through each element and place it in its correct position
    for cycle_start in range(0, len(arr) - 1):
        item = arr[cycle_start]

        # Find the position where we put the item. We count all smaller elements to find the correct position.
        pos = cycle_start
        for i in range(cycle_start + 1, len(arr)):
            if arr[i] < item:
                pos += 1

        # If the item is already in the correct position, continue to the next cycle
        if pos == cycle_start:
            continue

        # Skip duplicates
        while item == arr[pos]:
            pos += 1

        # Put the item to its right position
        arr[pos], item = item, arr[pos]

        # Rotate the rest of the cycle
        while pos != cycle_start:
            pos = cycle_start
            # Find the position where we put the item
            for i in range(cycle_start + 1, len(arr)):
                if arr[i] < item:
                    pos += 1

            # Skip duplicates
            while item == arr[pos]:
                pos += 1

            # Put the item to its right position
            arr[pos], item = item, arr[pos]

    # The array is sorted in place, so no return is necessary
    # This algorithm is efficient in terms of writes, making it suitable for scenarios where write operations are expensive.