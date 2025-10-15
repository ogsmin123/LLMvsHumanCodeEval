# Sentinel Linear Search Algorithm
def sentinel_linear_search(arr, key):
    """
    Perform a sentinel linear search on the given list to find the index of the key.
    
    :param arr: List of elements to search through.
    :param key: The element to search for.
    :return: The index of the key if found, otherwise -1.
    
    The sentinel linear search places a sentinel at the end of the list to avoid
    checking the bounds in each iteration, which can slightly improve performance.
    """
    n = len(arr)
    if n == 0:
        return -1  # Edge case: empty list, key cannot be found

    # Save the last element and place the key as a sentinel
    last = arr[-1]
    arr[-1] = key

    i = 0
    # Loop until we find the key
    while arr[i] != key:
        i += 1

    # Restore the last element
    arr[-1] = last

    # If the key is found and it's not the sentinel position, return the index
    if i < n - 1 or arr[-1] == key:
        return i
    else:
        return -1  # Key not found

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # Manual testing
    print(sentinel_linear_search([1, 2, 3, 4, 5], 3))  # Expected output: 2
    print(sentinel_linear_search([1, 2, 3, 4, 5], 6))  # Expected output: -1
    print(sentinel_linear_search([], 1))               # Expected output: -1
    print(sentinel_linear_search([1], 1))              # Expected output: 0
    print(sentinel_linear_search([1], 2))              # Expected output: -1