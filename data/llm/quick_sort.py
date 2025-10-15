# Quick sort implementation in Python

def quick_sort(arr):
    """
    Sorts an array using the quick sort algorithm.

    Args:
        arr (list): The list of elements to be sorted.

    Returns:
        list: A new list containing the sorted elements.

    The function uses the divide-and-conquer approach to sort the array.
    It selects a pivot element and partitions the array into two halves:
    elements less than the pivot and elements greater than the pivot.
    It recursively sorts the two halves and combines them with the pivot.
    """

    # Base case: if the array is empty or contains a single element, it's already sorted
    if len(arr) <= 1:
        return arr

    # Choose the pivot element; here, we choose the last element for simplicity
    pivot = arr[-1]

    # Partition the array into two halves: less than and greater than the pivot
    less_than_pivot = [x for x in arr[:-1] if x <= pivot]
    greater_than_pivot = [x for x in arr[:-1] if x > pivot]

    # Recursively sort the partitions and combine them with the pivot
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

if __name__ == "__main__":
    # Example usage and manual testing
    example_array = [3, 6, 8, 10, 1, 2, 1]
    print("Original array:", example_array)
    print("Sorted array:", quick_sort(example_array))

    # Edge case: empty array
    print("Sorted empty array:", quick_sort([]))

    # Edge case: array with one element
    print("Sorted single-element array:", quick_sort([42]))

    # Edge case: array with all identical elements
    print("Sorted identical elements array:", quick_sort([7, 7, 7, 7, 7]))

    # Edge case: already sorted array
    print("Sorted already sorted array:", quick_sort([1, 2, 3, 4, 5]))

    # Edge case: reverse sorted array
    print("Sorted reverse sorted array:", quick_sort([5, 4, 3, 2, 1]))