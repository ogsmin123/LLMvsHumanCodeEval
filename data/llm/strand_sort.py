def strand_sort(input_list):
    # Base case: if the list is empty or has one element, it's already sorted
    if len(input_list) <= 1:
        return input_list

    result = []  # This will store the final sorted list

    while input_list:
        # Start a new sublist with the first element of the input_list
        sublist = [input_list.pop(0)]

        # Iterate over the input_list to build the sublist
        i = 0
        while i < len(input_list):
            # If the current element is greater than the last element in the sublist
            if input_list[i] > sublist[-1]:
                # Append it to the sublist and remove from input_list
                sublist.append(input_list.pop(i))
            else:
                # Move to the next element
                i += 1

        # Merge the sublist into the result list
        result = merge(result, sublist)

    return result

def merge(left, right):
    # This function merges two sorted lists into a single sorted list
    result = []
    i = j = 0

    # Iterate over both lists and append the smaller element to the result
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements from both lists
    result.extend(left[i:])
    result.extend(right[j:])

    return result