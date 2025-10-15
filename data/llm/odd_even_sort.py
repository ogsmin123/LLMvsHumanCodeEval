def odd_even_sort(arr):
    n = len(arr)
    is_sorted = False
    
    while not is_sorted:
        is_sorted = True
        
        # Perform Bubble sort on odd indexed elements
        for i in range(1, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False
        
        # Perform Bubble sort on even indexed elements
        for i in range(0, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False
    
    return arr

# The function implements the odd-even sort (brick sort) algorithm.
# It alternates between sorting odd indexed pairs and even indexed pairs.
# The process continues until the array is sorted, indicated by no swaps in a full pass.
# This approach is simple but not the most efficient for large datasets.