def exchange_sort(arr):
    """
    Sorts an array using the exchange sort algorithm.

    :param arr: List of elements to be sorted.
    :return: Sorted list.
    """
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(i + 1, n):
            # Swap if the element found is greater than the next element
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

# The exchange sort algorithm is a simple sorting algorithm that works by repeatedly
# comparing and swapping adjacent elements if they are in the wrong order.
# It is not efficient for large datasets as its average and worst-case time complexity
# is O(n^2), where n is the number of items being sorted. However, it is easy to implement
# and can be useful for small datasets or educational purposes.