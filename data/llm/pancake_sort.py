# Pancake sort algorithm implementation
def pancake_sort(arr):
    """
    Sorts an array using the pancake sort algorithm.
    
    The algorithm works by repeatedly flipping the largest unsorted element to the end of the unsorted section.
    
    :param arr: List of integers to be sorted.
    :return: The sorted list.
    
    >>> pancake_sort([3, 2, 4, 1])
    [1, 2, 3, 4]
    >>> pancake_sort([1, 5, 4, 3, 2])
    [1, 2, 3, 4, 5]
    >>> pancake_sort([])
    []
    >>> pancake_sort([1])
    [1]
    >>> pancake_sort([2, 1])
    [1, 2]
    """
    def flip(sub_arr, k):
        """Reverses the order of the first k elements of the array."""
        # Flipping is done by reversing the sublist from 0 to k
        sub_arr[:k] = reversed(sub_arr[:k])

    n = len(arr)
    for size in range(n, 1, -1):
        # Find the index of the maximum element in the unsorted section
        max_index = max(range(size), key=arr.__getitem__)
        if max_index != size - 1:
            # Flip the maximum element to the front if it's not already there
            flip(arr, max_index + 1)
            # Flip it to its correct position at the end of the unsorted section
            flip(arr, size)
    return arr

if __name__ == "__main__":
    import doctest
    doctest.testmod()