def double_sort(arr):
    """
    Sorts an array such that all even numbers are sorted in ascending order
    and all odd numbers are sorted in descending order, while maintaining
    their relative positions.
    
    Parameters:
    arr (list of int): The list of integers to be sorted.
    
    Returns:
    list of int: The sorted list with evens in ascending order and odds in descending order.
    """
    # Separate even and odd numbers
    evens = [x for x in arr if x % 2 == 0]
    odds = [x for x in arr if x % 2 != 0]
    
    # Sort evens in ascending order and odds in descending order
    evens.sort()
    odds.sort(reverse=True)
    
    # Merge sorted evens and odds back into the original array structure
    result = []
    even_index, odd_index = 0, 0
    
    for num in arr:
        if num % 2 == 0:
            # Append the next sorted even number
            result.append(evens[even_index])
            even_index += 1
        else:
            # Append the next sorted odd number
            result.append(odds[odd_index])
            odd_index += 1
    
    return result

# Example usage:
# double_sort([5, 3, 2, 8, 1, 4]) should return [2, 8, 4, 5, 3, 1]