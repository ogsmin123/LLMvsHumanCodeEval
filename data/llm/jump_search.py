def jump_search(arr, x):
    """
    Perform jump search on a sorted array to find the index of element x.
    
    Parameters:
    arr (list): A sorted list of elements.
    x (int/float): The element to search for in the list.
    
    Returns:
    int: The index of element x if found, otherwise -1.
    """
    import math

    n = len(arr)
    # Calculate the optimal jump size as the square root of the array length
    step = int(math.sqrt(n))
    prev = 0

    # Jump through the array in blocks of size 'step'
    while prev < n and arr[min(step, n) - 1] < x:
        prev = step
        step += int(math.sqrt(n))
        # If we've jumped past the end of the array, x is not present
        if prev >= n:
            return -1

    # Perform a linear search in the block where x could be present
    for i in range(prev, min(step, n)):
        if arr[i] == x:
            return i

    # If we reach here, x is not present in the array
    return -1