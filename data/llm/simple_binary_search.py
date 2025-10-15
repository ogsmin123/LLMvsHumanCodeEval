"""
A pure Python implementation of a binary search algorithm.

Binary search is a classic algorithm for finding a target value within a sorted array.
It operates by repeatedly dividing the search interval in half. If the value of the
search key is less than the item in the middle of the interval, the search continues
in the lower half, or if greater, in the upper half. This process repeats until the
target value is found or the interval is empty.

For doctests, run the following command:
python3 -m doctest -v simple_binary_search.py

For manual testing, run:
python3 simple_binary_search.py
"""

from typing import List, Any

def binary_search(arr: List[Any], target: Any) -> int:
    """
    Perform a binary search on a sorted list to find the index of the target value.

    :param arr: A list of elements sorted in ascending order.
    :param target: The element to search for in the list.
    :return: The index of the target element if found, otherwise -1.

    >>> binary_search([1, 2, 3, 4, 5], 3)
    2
    >>> binary_search([1, 2, 3, 4, 5], 6)
    -1
    >>> binary_search([], 3)
    -1
    >>> binary_search([1], 1)
    0
    >>> binary_search([1, 2, 3, 4, 5], 1)
    0
    >>> binary_search([1, 2, 3, 4, 5], 5)
    4
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Avoids potential overflow
        # Check if the middle element is the target
        if arr[mid] == target:
            return mid
        # If target is greater, ignore the left half
        elif arr[mid] < target:
            left = mid + 1
        # If target is smaller, ignore the right half
        else:
            right = mid - 1

    # Target was not found in the list
    return -1

if __name__ == "__main__":
    # Manual testing
    test_array = [1, 2, 3, 4, 5]
    test_target = 3
    result = binary_search(test_array, test_target)
    print(f"Index of {test_target} in {test_array} is {result}")
    
    test_target = 6
    result = binary_search(test_array, test_target)
    print(f"Index of {test_target} in {test_array} is {result}")