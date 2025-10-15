import sys

def pigeon_sort(arr):
    if not arr:
        return arr

    # Find the minimum and maximum values to determine the range
    min_val = min(arr)
    max_val = max(arr)
    size = max_val - min_val + 1

    # Create an array of empty lists to hold the "pigeons"
    holes = [[] for _ in range(size)]

    # Place each element in its respective hole
    for number in arr:
        holes[number - min_val].append(number)

    # Flatten the list of holes into a sorted array
    sorted_arr = []
    for hole in holes:
        sorted_arr.extend(hole)

    return sorted_arr

if __name__ == "__main__":
    # Example usage and manual testing
    example_array = [8, 3, 2, 7, 4, 6, 8]
    print("Original array:", example_array)
    sorted_array = pigeon_sort(example_array)
    print("Sorted array:", sorted_array)

    # Edge case: empty array
    empty_array = []
    print("Empty array sorted:", pigeon_sort(empty_array))

    # Edge case: array with one element
    single_element_array = [5]
    print("Single element array sorted:", pigeon_sort(single_element_array))

    # Edge case: array with all identical elements
    identical_elements_array = [9, 9, 9, 9]
    print("Identical elements array sorted:", pigeon_sort(identical_elements_array))

    # Edge case: array with negative numbers
    negative_numbers_array = [-5, -1, -3, -2, -4]
    print("Negative numbers array sorted:", pigeon_sort(negative_numbers_array))