import random

def is_sorted(data):
    """Check if the list is sorted in non-decreasing order."""
    for i in range(len(data) - 1):
        if data[i] > data[i + 1]:
            return False
    return True

def bogo_sort(data):
    """Sort the list using the bogosort algorithm.
    
    Bogosort is a highly inefficient sorting algorithm based on the generate and test paradigm.
    It successively generates permutations of its input until it finds one that is sorted.
    """
    while not is_sorted(data):
        random.shuffle(data)  # Randomly shuffle the list
    return data

if __name__ == "__main__":
    # Example usage
    data = [3, 2, 5, 1, 4]
    print("Unsorted:", data)
    sorted_data = bogo_sort(data)
    print("Sorted:", sorted_data)