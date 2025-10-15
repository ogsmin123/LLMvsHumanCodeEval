def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Keep track of whether any swaps were made in this pass
        swapped = False
        # Last i elements are already sorted, so skip them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no two elements were swapped by inner loop, then break
        if not swapped:
            break
    return arr

# The function sorts the array in place and returns it.
# It uses a flag to optimize the algorithm by stopping early if the array becomes sorted before completing all passes.
# This optimization makes it more efficient for nearly sorted arrays.