# Patience sorting algorithm implementation using stacks.
# Patience sorting is inspired by the card game "patience" or "solitaire".
# The algorithm sorts a sequence by distributing elements into piles (stacks),
# then merges the piles to produce a sorted sequence.

def patience_sort(sequence):
    # Helper function to find the position to place the element in the piles
    def find_position(piles, element):
        low, high = 0, len(piles)
        while low < high:
            mid = (low + high) // 2
            if piles[mid][-1] < element:
                low = mid + 1
            else:
                high = mid
        return low

    # Create piles (stacks) to hold the sorted subsequences
    piles = []
    for element in sequence:
        pos = find_position(piles, element)
        if pos == len(piles):
            # Create a new pile if no suitable pile is found
            piles.append([element])
        else:
            # Place the element on top of the found pile
            piles[pos].append(element)

    # Merge the piles to form the sorted sequence
    result = []
    while piles:
        # Find the smallest top element among all piles
        smallest = min(pile[-1] for pile in piles)
        result.append(smallest)
        # Remove the smallest element from its pile
        for pile in piles:
            if pile[-1] == smallest:
                pile.pop()
                if not pile:
                    # Remove empty piles
                    piles.remove(pile)
                break

    return result

# Example usage:
# sorted_sequence = patience_sort([4, 3, 2, 1, 5, 6, 7, 0])
# print(sorted_sequence)  # Output: [0, 1, 2, 3, 4, 5, 6, 7]