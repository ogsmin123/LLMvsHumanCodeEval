# Problem: radix_sort
# Description: This is a pure Python implementation of the radix sort algorithm.
# For doctests run following command:
# python -m doctest -v radix_sort.py
# or
# python3 -m doctest -v radix_sort.py
# For manual testing run:
# python radix_sort.py

def radix_sort(arr):
    """
    Perform radix sort on a list of non-negative integers.

    Radix sort is a non-comparative integer sorting algorithm that sorts data with integer keys
    by grouping keys by the individual digits which share the same significant position and value.

    Args:
    arr (list): List of non-negative integers to be sorted.

    Returns:
    list: Sorted list of integers.

    Example:
    >>> radix_sort([170, 45, 75, 90, 802, 24, 2, 66])
    [2, 24, 45, 66, 75, 90, 170, 802]
    """
    if not arr:
        return arr  # Return early if the list is empty

    # Find the maximum number to know the number of digits
    max_num = max(arr)

    # Initialize the exponent to 1 (10^0)
    exp = 1

    # Perform counting sort for every digit
    while max_num // exp > 0:
        arr = counting_sort(arr, exp)
        exp *= 10  # Move to the next significant digit

    return arr

def counting_sort(arr, exp):
    """
    A helper function to perform counting sort based on the digit represented by exp.

    Args:
    arr (list): List of non-negative integers to be sorted.
    exp (int): The exponent corresponding to the digit position to sort by.

    Returns:
    list: Partially sorted list of integers based on the current digit.
    """
    n = len(arr)
    output = [0] * n  # Output array to store sorted numbers
    count = [0] * 10  # Count array to store the count of occurrences of digits (0-9)

    # Store the count of occurrences of each digit in count[]
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Change count[i] so that it contains the actual position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    return output

if __name__ == "__main__":
    import doctest
    doctest.testmod()