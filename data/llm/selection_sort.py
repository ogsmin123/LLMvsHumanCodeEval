# Implementation of the selection sort algorithm in Python
def selection_sort(arr):
    """
    Sorts an array using the selection sort algorithm.

    Args:
    arr (list): A list of elements to be sorted.

    Returns:
    list: The sorted list.

    The function sorts the list in place and returns it for convenience.
    """
    n = len(arr)
    for i in range(n):
        # Assume the minimum is the first element
        min_idx = i
        # Iterate over the unsorted elements
        for j in range(i + 1, n):
            # Update min_idx if a smaller element is found
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first unsorted element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # Manual testing
    print(selection_sort([64, 25, 12, 22, 11]))  # Output should be [11, 12, 22, 25, 64]
    print(selection_sort([5, 3, 8, 6, 2]))      # Output should be [2, 3, 5, 6, 8]
    print(selection_sort([]))                   # Output should be []
    print(selection_sort([1]))                  # Output should be [1]
    print(selection_sort([2, 1]))               # Output should be [1, 2]