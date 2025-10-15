def wiggle_sort(nums):
    # Iterate over the array, adjusting elements to satisfy the wiggle property
    for i in range(len(nums) - 1):
        # If the current index is even, ensure nums[i] < nums[i + 1]
        if i % 2 == 0:
            if nums[i] > nums[i + 1]:
                # Swap to maintain the wiggle property
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        else:
            # If the current index is odd, ensure nums[i] > nums[i + 1]
            if nums[i] < nums[i + 1]:
                # Swap to maintain the wiggle property
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

# Example usage:
nums = [3, 5, 2, 1, 6, 4]
wiggle_sort(nums)
print(nums)  # Output should be a valid wiggle sorted array, e.g., [3, 5, 1, 6, 2, 4]