def msd_radix_sort(arr):
    # Helper function to perform the sorting based on the current bit position
    def sort_by_bit(arr, bit):
        if len(arr) <= 1 or bit < 0:
            return arr
        
        # Partition the array into two lists: one for 0s and one for 1s at the current bit position
        zero_bucket = []
        one_bucket = []
        
        for num in arr:
            # Check the bit at the current position
            if (num >> bit) & 1:
                one_bucket.append(num)
            else:
                zero_bucket.append(num)
        
        # Recursively sort both partitions and concatenate the results
        return sort_by_bit(zero_bucket, bit - 1) + sort_by_bit(one_bucket, bit - 1)
    
    if not arr:
        return arr
    
    # Find the maximum number to determine the number of bits needed
    max_num = max(arr)
    max_bit = max_num.bit_length() - 1  # Get the index of the most significant bit
    
    # Start sorting from the most significant bit
    return sort_by_bit(arr, max_bit)

# Example usage:
# sorted_array = msd_radix_sort([3, 6, 2, 8, 5, 1])
# print(sorted_array)  # Output should be a sorted list [1, 2, 3, 5, 6, 8]