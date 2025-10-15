# Counting Sort Implementation in Python

def counting_sort(arr):
    """
    Perform counting sort on the input list `arr`.

    :param arr: List of integers to sort
    :return: A new list containing the sorted integers

    The function assumes that all integers in `arr` are non-negative.
    """
    if not arr:
        return arr  # Return empty list if input is empty

    # Find the maximum value in the array to determine the range of counts
    max_val = max(arr)

    # Initialize count array with zeros, with a size of max_val + 1
    count = [0] * (max_val + 1)

    # Populate the count array where each index represents an integer in `arr`
    for num in arr:
        count[num] += 1

    # Create the sorted output array
    sorted_arr = []
    for num, freq in enumerate(count):
        sorted_arr.extend([num] * freq)  # Append `num` `freq` times

    return sorted_arr

if __name__ == "__main__":
    # Example usage and manual testing
    example_arr = [4, 2, 2, 8, 3, 3, 1]
    print("Original array:", example_arr)
    print("Sorted array:", counting_sort(example_arr))

    # Additional test cases
    assert counting_sort([]) == []
    assert counting_sort([1]) == [1]
    assert counting_sort([3, 3, 3]) == [3, 3, 3]
    assert counting_sort([9, 7, 5, 3, 1]) == [1, 3, 5, 7, 9]
    assert counting_sort([5, 4, 3, 2, 1, 0]) == [0, 1, 2, 3, 4, 5]

    print("All tests passed.")