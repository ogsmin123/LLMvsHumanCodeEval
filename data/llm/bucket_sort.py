#!/usr/bin/env python3

def bucket_sort(arr):
    """Sorts an array of numbers using the bucket sort algorithm."""
    if len(arr) == 0:
        return arr  # Edge case: empty array is already sorted

    # Determine minimum and maximum values to define the range of the buckets
    min_value, max_value = min(arr), max(arr)
    bucket_count = len(arr)
    
    # Edge case: if all elements are the same, return the array as is
    if min_value == max_value:
        return arr

    # Initialize buckets
    buckets = [[] for _ in range(bucket_count)]

    # Distribute input array values into buckets
    for num in arr:
        # Calculate index for the bucket
        index = int((num - min_value) / (max_value - min_value) * (bucket_count - 1))
        buckets[index].append(num)

    # Sort each bucket and concatenate the results
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(sorted(bucket))  # Using built-in sort for simplicity

    return sorted_array

# Example usage:
if __name__ == "__main__":
    example_array = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
    print(bucket_sort(example_array))  # Output should be a sorted version of example_array