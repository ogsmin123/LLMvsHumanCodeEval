# Implementation of the merge sort algorithm in Python

def merge_sort(arr):
    """
    Sorts an array using the merge sort algorithm.
    
    :param arr: List of elements to be sorted.
    :return: A new list containing all elements from arr in sorted order.
    
    The function uses a divide-and-conquer approach to recursively split the array
    into halves, sort each half, and then merge the sorted halves back together.
    """
    if len(arr) <= 1:
        # Base case: a list of zero or one elements is already sorted
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    """
    Merges two sorted lists into a single sorted list.
    
    :param left: First sorted list.
    :param right: Second sorted list.
    :return: A merged and sorted list containing all elements from left and right.
    
    This function iterates over both input lists, repeatedly taking the smallest
    element from the front of each list and appending it to the result list.
    """
    result = []
    left_index, right_index = 0, 0

    # Continue merging until one of the lists is exhausted
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Append any remaining elements from the left list
    result.extend(left[left_index:])
    # Append any remaining elements from the right list
    result.extend(right[right_index:])

    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # Example usage
    example_array = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", example_array)
    sorted_array = merge_sort(example_array)
    print("Sorted array:", sorted_array)