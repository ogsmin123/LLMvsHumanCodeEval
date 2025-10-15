def gnome_sort(arr):
    """
    Sorts a list using the Gnome Sort algorithm.
    
    Gnome Sort is a simple comparison-based sorting algorithm. It iterates over the list, and whenever it finds two 
    consecutive elements that are out of order, it swaps them and moves one step back. If the elements are in order, 
    it moves one step forward. The process continues until the end of the list is reached.
    
    This algorithm has a time complexity of O(n^2) in the worst case, similar to bubble sort and insertion sort, 
    but it can be efficient for small lists or lists that are already partially sorted.
    
    Parameters:
    arr (list): The list of elements to be sorted. The list is sorted in place.
    
    Returns:
    None: The function modifies the list in place and returns None.
    
    Example:
    >>> arr = [34, 2, 10, -9]
    >>> gnome_sort(arr)
    >>> arr
    [-9, 2, 10, 34]
    """
    index = 0
    while index < len(arr):
        # If we are at the start of the list or the current element is in order with the previous one, move forward
        if index == 0 or arr[index] >= arr[index - 1]:
            index += 1
        else:
            # Swap the elements if they are out of order
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            # Move one step back to check the new order
            index -= 1