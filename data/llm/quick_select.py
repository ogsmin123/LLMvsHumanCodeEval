# The quick select algorithm is used to find the k-th smallest element in an unordered list.
# It is similar to the quicksort algorithm, but instead of sorting the entire list, it only partially sorts the list
# until the k-th smallest element is found. This makes it more efficient than sorting the entire list when only
# the k-th smallest element is needed.

import random

def quick_select(arr, k):
    """
    Find the k-th smallest element in an unordered list using the quick select algorithm.
    
    :param arr: List of elements to search through.
    :param k: The index (0-based) of the smallest element to find.
    :return: The k-th smallest element in the list.
    """
    if arr is None or len(arr) == 0:
        raise ValueError("Array cannot be None or empty")
    if k < 0 or k >= len(arr):
        raise IndexError("k is out of bounds of the array")

    def partition(left, right, pivot_index):
        pivot_value = arr[pivot_index]
        # Move pivot to end
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
        store_index = left
        # Move all smaller elements to the left
        for i in range(left, right):
            if arr[i] < pivot_value:
                arr[store_index], arr[i] = arr[i], arr[store_index]
                store_index += 1
        # Move pivot to its final place
        arr[right], arr[store_index] = arr[store_index], arr[right]
        return store_index

    def select(left, right, k_smallest):
        """
        Returns the k-th smallest element of list within left..right.
        """
        if left == right:  # If the list contains only one element
            return arr[left]

        # Select a random pivot_index between left and right
        pivot_index = random.randint(left, right)

        # Find the pivot position in a sorted list
        pivot_index = partition(left, right, pivot_index)

        # The pivot is in its final sorted position
        if k_smallest == pivot_index:
            return arr[k_smallest]
        elif k_smallest < pivot_index:
            # Go left
            return select(left, pivot_index - 1, k_smallest)
        else:
            # Go right
            return select(pivot_index + 1, right, k_smallest)

    return select(0, len(arr) - 1, k)

# The function quick_select is designed to handle edge cases such as:
# - An empty array or None input, which raises a ValueError.
# - An out-of-bounds k, which raises an IndexError.
# The use of a random pivot helps to ensure average-case O(n) performance, even though the worst-case is O(n^2).