# The task is to implement a recursive linear search algorithm that searches for a given element in a list and returns its index.
# If the element is not found, the function should return -1.

def linear_search_recursive(arr, target, index=0):
    # Base case: If the index reaches the length of the array, the target is not found.
    if index >= len(arr):
        return -1
    
    # If the current element matches the target, return the current index.
    if arr[index] == target:
        return index
    
    # Recur for the next element in the array.
    return linear_search_recursive(arr, target, index + 1)

# This function is designed to handle the edge case where the array is empty by immediately returning -1.
# It also handles the case where the target is not present in the array by returning -1 when the recursion reaches the end of the array.
# The function uses a default parameter `index` to keep track of the current position in the array during recursion.