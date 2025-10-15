# Bitonic Sort implementation in Python
# This implementation assumes that the input size is a power of 2.

def bitonic_sort(arr):
    """Sorts an array using the Bitonic Sort algorithm."""
    def compare_and_swap(arr, i, j, direction):
        """Compares and swaps elements if they are not in the desired order."""
        if (direction == 1 and arr[i] > arr[j]) or (direction == 0 and arr[i] < arr[j]):
            arr[i], arr[j] = arr[j], arr[i]

    def bitonic_merge(arr, low, cnt, direction):
        """Merges bitonic sequences in the specified direction."""
        if cnt > 1:
            k = cnt // 2
            for i in range(low, low + k):
                compare_and_swap(arr, i, i + k, direction)
            bitonic_merge(arr, low, k, direction)
            bitonic_merge(arr, low + k, k, direction)

    def bitonic_sort_recursive(arr, low, cnt, direction):
        """Recursively sorts a bitonic sequence."""
        if cnt > 1:
            k = cnt // 2
            # Sort in ascending order
            bitonic_sort_recursive(arr, low, k, 1)
            # Sort in descending order
            bitonic_sort_recursive(arr, low + k, k, 0)
            # Merge the entire sequence in the specified direction
            bitonic_merge(arr, low, cnt, direction)

    # Start the recursive bitonic sort
    bitonic_sort_recursive(arr, 0, len(arr), 1)

# Example usage:
# arr = [3, 7, 4, 8, 6, 2, 1, 5]
# bitonic_sort(arr)
# print(arr)  # Output will be a sorted array

# The code assumes that the length of the array is a power of 2. If the input size is not a power of 2,
# the behavior is undefined. This is a trade-off for simplicity and efficiency, as bitonic sort is
# designed for parallel execution and works optimally with sizes that are powers of 2.