#!/usr/bin/env python3

def binary_search(arr, target):
    """
    Perform a binary search on a sorted array to find the index of the target element.
    
    :param arr: List[int] - A list of integers sorted in ascending order.
    :param target: int - The target integer to search for in the array.
    :return: int - The index of the target element if found; otherwise, -1.
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # Calculate the middle index to avoid overflow
        
        # Check if the middle element is the target
        if arr[mid] == target:
            return mid
        # If the target is greater, ignore the left half
        elif arr[mid] < target:
            left = mid + 1
        # If the target is smaller, ignore the right half
        else:
            right = mid - 1
    
    # Target is not present in the array
    return -1

# Example usage:
# result = binary_search([1, 2, 3, 4, 5], 3)
# print(result)  # Output: 2