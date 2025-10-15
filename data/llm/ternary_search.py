def ternary_search(arr, target, precision=10):
    """
    Perform a ternary search on a sorted array to find the target value.
    
    :param arr: List of elements to search through. Must be sorted.
    :param target: The value to search for.
    :param precision: The threshold for switching to linear search.
    :return: The index of the target in the array, or -1 if not found.
    """
    left, right = 0, len(arr) - 1

    while right - left > precision:
        # Calculate the two mid points
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        # Check if target is at any mid point
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2

        # Narrow down the search space based on the target's position
        if target < arr[mid1]:
            right = mid1 - 1
        elif target > arr[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1

    # Perform linear search when the search space is small
    for i in range(left, right + 1):
        if arr[i] == target:
            return i

    return -1