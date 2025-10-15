#!/usr/bin/env python

import os
import heapq
import tempfile

def external_sort(input_file_path, output_file_path, chunk_size=100000):
    """
    Sorts a large text file using external sorting to minimize memory usage.
    
    :param input_file_path: Path to the input file to be sorted.
    :param output_file_path: Path where the sorted output file will be saved.
    :param chunk_size: Number of lines to read into memory at a time.
    """
    # Create a temporary directory to store sorted chunks
    temp_dir = tempfile.mkdtemp()
    chunk_files = []

    try:
        # Read the input file in chunks
        with open(input_file_path, 'r') as input_file:
            while True:
                lines = input_file.readlines(chunk_size)
                if not lines:
                    break

                # Sort each chunk in memory
                lines.sort()

                # Write the sorted chunk to a temporary file
                temp_chunk_file = tempfile.NamedTemporaryFile(delete=False, dir=temp_dir, mode='w')
                temp_chunk_file.writelines(lines)
                temp_chunk_file.close()
                chunk_files.append(temp_chunk_file.name)

        # Merge sorted chunks and write to the output file
        with open(output_file_path, 'w') as output_file:
            # Open all chunk files for reading
            open_files = [open(chunk_file, 'r') for chunk_file in chunk_files]

            # Use a heap to merge the sorted chunks efficiently
            heap = []
            for file_index, open_file in enumerate(open_files):
                line = open_file.readline()
                if line:
                    heapq.heappush(heap, (line, file_index))

            while heap:
                # Get the smallest line from the heap
                smallest_line, file_index = heapq.heappop(heap)
                output_file.write(smallest_line)

                # Read the next line from the same file and add it to the heap
                next_line = open_files[file_index].readline()
                if next_line:
                    heapq.heappush(heap, (next_line, file_index))

            # Close all open files
            for open_file in open_files:
                open_file.close()

    finally:
        # Clean up temporary files
        for chunk_file in chunk_files:
            os.remove(chunk_file)
        os.rmdir(temp_dir)

# Example usage:
# external_sort('large_input.txt', 'sorted_output.txt')