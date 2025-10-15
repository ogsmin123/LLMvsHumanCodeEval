def bead_sort(sequence):
    # Bead sort only works for non-negative integers
    if any(x < 0 for x in sequence):
        raise ValueError("Bead sort only works for non-negative integers.")

    # The maximum value in the sequence determines the number of "beads" (levels)
    max_value = max(sequence, default=0)

    # Each level in the grid represents a bead; initialize the grid
    grid = [[0] * len(sequence) for _ in range(max_value)]

    # Drop beads down the grid
    for i, num in enumerate(sequence):
        for j in range(num):
            grid[j][i] = 1

    # Collect the sorted sequence by counting beads at each level
    sorted_sequence = []
    for level in grid:
        sorted_sequence.append(sum(level))

    return sorted_sequence

# The function handles edge cases like empty input and sequences with zero values.
# It raises an error for negative numbers, as bead sort is not defined for them.
# The grid is constructed with dimensions based on the maximum value in the sequence,
# ensuring that the algorithm is efficient in both time and space for the input size.