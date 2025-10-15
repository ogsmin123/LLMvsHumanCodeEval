def interpolation_search(arr, x):
    """
    Perform interpolation search on a sorted array to find the index of a given element.
    
    :param arr: List of elements sorted in ascending order.
    :param x: The element to search for.
    :return: The index of the element if found, otherwise -1.
    """
    low = 0
    high = len(arr) - 1

    while low <= high and x >= arr[low] and x <= arr[high]:
        # Avoid division by zero if arr[high] == arr[low]
        if arr[low] == arr[high]:
            if arr[low] == x:
                return low
            else:
                return -1

        # Estimate the position of the search key using interpolation formula
        pos = low + ((high - low) * (x - arr[low]) // (arr[high] - arr[low]))

        # Check if the estimated position is the target
        if arr[pos] == x:
            return pos

        # If x is larger, x is in the upper part
        if arr[pos] < x:
            low = pos + 1
        # If x is smaller, x is in the lower part
        else:
            high = pos - 1

    return -1  # Element not found

# This implementation assumes that the input array is sorted in ascending order.
# It uses the interpolation formula to estimate the position of the target element,
# which can be more efficient than binary search for uniformly distributed data.
# Edge cases handled include division by zero when all elements are the same and
# the target is not present.