import sys
from typing import List

def introsort(arr: List[int]) -> None:
    # Entry point for introsort, calculates depth limit and calls the recursive function
    max_depth = (len(arr).bit_length() - 1) * 2
    _introsort_helper(arr, 0, len(arr) - 1, max_depth)

def _introsort_helper(arr: List[int], start: int, end: int, max_depth: int) -> None:
    # Helper function for introsort, switches between quicksort and heapsort based on depth
    if end - start < 16:
        _insertion_sort(arr, start, end)
    elif max_depth == 0:
        _heap_sort(arr, start, end)
    else:
        pivot = _partition(arr, start, end)
        _introsort_helper(arr, start, pivot - 1, max_depth - 1)
        _introsort_helper(arr, pivot + 1, end, max_depth - 1)

def _insertion_sort(arr: List[int], start: int, end: int) -> None:
    # Simple insertion sort for small subarrays
    for i in range(start + 1, end + 1):
        key = arr[i]
        j = i - 1
        while j >= start and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def _heap_sort(arr: List[int], start: int, end: int) -> None:
    # Heapsort for large subarrays when recursion depth is exceeded
    _build_max_heap(arr, start, end)
    for i in range(end, start, -1):
        arr[start], arr[i] = arr[i], arr[start]
        _max_heapify(arr, index=start, end=i - 1)

def _build_max_heap(arr: List[int], start: int, end: int) -> None:
    # Builds a max heap from the array
    length = end - start + 1
    for i in range(length // 2 - 1, -1, -1):
        _max_heapify(arr, start + i, end)

def _max_heapify(arr: List[int], index: int, end: int) -> None:
    # Maintains the max heap property
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2
    if left <= end and arr[left] > arr[largest]:
        largest = left
    if right <= end and arr[right] > arr[largest]:
        largest = right
    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        _max_heapify(arr, largest, end)

def _partition(arr: List[int], start: int, end: int) -> int:
    # Partition function for quicksort
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1