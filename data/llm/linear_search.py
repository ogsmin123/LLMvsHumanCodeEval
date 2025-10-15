# Linear Search Algorithm
# This function performs a linear search on a list to find the index of a target element.
# It returns the index of the target if found, otherwise it returns -1.
def linear_search(arr, target):
    """
    Perform a linear search for the target in the given list.

    :param arr: List of elements to search through.
    :param target: The element to search for.
    :return: The index of the target element if found, otherwise -1.

    >>> linear_search([1, 2, 3, 4, 5], 3)
    2
    >>> linear_search([1, 2, 3, 4, 5], 6)
    -1
    >>> linear_search([], 1)
    -1
    >>> linear_search([5], 5)
    0
    >>> linear_search([5], 1)
    -1
    """
    # Iterate over each element in the list along with its index
    for index, element in enumerate(arr):
        # Check if the current element is the target
        if element == target:
            return index  # Return the index if the target is found
    return -1  # Return -1 if the target is not found in the list

if __name__ == "__main__":
    import doctest
    doctest.testmod()  # Run the doctests to verify the implementation

    # Example of manual testing
    print(linear_search([10, 20, 30, 40, 50], 30))  # Expected output: 2
    print(linear_search([10, 20, 30, 40, 50], 60))  # Expected output: -1
    print(linear_search([], 10))  # Expected output: -1
    print(linear_search([10], 10))  # Expected output: 0
    print(linear_search([10], 20))  # Expected output: -1