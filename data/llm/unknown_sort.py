# The unknown_sort function sorts a list using a selection sort-like approach.
# It repeatedly finds the minimum element and removes it from the list, appending it to the sorted list.
# This approach has a best-case time complexity of O(n) and a worst-case time complexity of O(n^2).

def unknown_sort(arr):
    sorted_arr = []
    while arr:
        # Find the minimum element in the list
        min_element = min(arr)
        # Remove the minimum element from the original list
        arr.remove(min_element)
        # Append the minimum element to the sorted list
        sorted_arr.append(min_element)
    return sorted_arr

# This function is not efficient for large lists due to its O(n^2) worst-case complexity.
# It is simple and leverages Python's built-in min and remove functions for clarity.