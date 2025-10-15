# Comb sort implementation in Python

def comb_sort(arr):
    # Initialize gap size to the length of the array
    gap = len(arr)
    # Set the shrink factor; 1.3 is a commonly used value
    shrink = 1.3
    # Initialize swapped to True to enter the while loop
    swapped = True

    # Continue sorting until the gap is 1 and no swaps are made
    while gap > 1 or swapped:
        # Calculate the new gap size
        gap = int(gap / shrink)
        # Ensure the gap is at least 1
        if gap < 1:
            gap = 1

        # Reset swapped to False to check if a swap occurs in this pass
        swapped = False

        # Perform a "comb" pass over the array
        for i in range(len(arr) - gap):
            # Compare elements that are 'gap' distance apart
            if arr[i] > arr[i + gap]:
                # Swap if they are in the wrong order
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                # Set swapped to True to indicate a swap occurred
                swapped = True

    # The array is now sorted
    return arr

# Example usage:
# sorted_array = comb_sort([64, 34, 25, 12, 22, 11, 90])
# print(sorted_array)