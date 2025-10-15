# Implementation of the heap sort algorithm using the standard library only.

def heapify(arr, n, i):
    """Helper function to maintain the heap property of a subtree rooted at index i.
    
    Args:
        arr (list): The list representing the heap.
        n (int): The size of the heap.
        i (int): The index of the root of the subtree.
    
    This function assumes that the binary trees rooted at left and right children of i
    are already heaps, but arr[i] might be smaller than its children, violating the heap
    property. The function ensures that the subtree rooted at i becomes a heap.
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left = 2*i + 1
    right = 2 * i + 2  # right = 2*i + 2

    # If left child is larger than root
    if left < n and arr[i] < arr[left]:
        largest = left

    # If right child is larger than largest so far
    if right < n and arr[largest] < arr[right]:
        largest = right

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Recursively heapify the affected subtree
        heapify(arr, n, largest)

def heap_sort(arr):
    """Main function to perform heap sort on a list.
    
    Args:
        arr (list): The list to be sorted.
    
    This function first builds a max heap from the input list. Then, it repeatedly extracts
    the maximum element from the heap (which is at the root), places it at the end of the list,
    and reduces the size of the heap by one. The heap property is maintained after each extraction.
    """
    n = len(arr)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # Example usage:
    arr = [12, 11, 13, 5, 6, 7]
    print("Unsorted array is:", arr)
    heap_sort(arr)
    print("Sorted array is:", arr)