# Pure Python implementation of Fibonacci Search
# This algorithm is used to find an element in a sorted array.
# It uses Fibonacci numbers to divide the array into sections.
# Resources: https://en.wikipedia.org/wiki/Fibonacci_search_technique

def fibonacci_search(arr, x):
    """
    Perform a Fibonacci search on a sorted array to find the index of a given element.

    :param arr: List[int] - A sorted list of integers where we need to find the element.
    :param x: int - The element to search for in the array.
    :return: int - The index of the element if found, otherwise -1.

    The function uses Fibonacci numbers to divide the array into sections.
    It is an efficient search algorithm with a time complexity of O(log n).
    """

    # Initialize the first two Fibonacci numbers
    fib_m2 = 0  # (m-2)'th Fibonacci number
    fib_m1 = 1  # (m-1)'th Fibonacci number
    fib_m = fib_m2 + fib_m1  # m'th Fibonacci number

    # fib_m is going to store the smallest Fibonacci number greater than or equal to len(arr)
    while fib_m < len(arr):
        fib_m2 = fib_m1
        fib_m1 = fib_m
        fib_m = fib_m2 + fib_m1

    # Marks the eliminated range from front
    offset = -1

    # While there are elements to be inspected, compare the element at index fib_m2 with x
    while fib_m > 1:
        # Check if fib_m2 is a valid location
        i = min(offset + fib_m2, len(arr) - 1)

        # If x is greater than the value at index fib_m2, cut the subarray array from offset to i
        if arr[i] < x:
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            offset = i

        # If x is less than the value at index fib_m2, cut the subarray after i+1
        elif arr[i] > x:
            fib_m = fib_m2
            fib_m1 = fib_m1 - fib_m2
            fib_m2 = fib_m - fib_m1

        # Element found. Return index
        else:
            return i

    # Compare the last element with x
    if fib_m1 and offset + 1 < len(arr) and arr[offset + 1] == x:
        return offset + 1

    # Element not found. Return -1
    return -1

if __name__ == "__main__":
    # Example usage
    arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
    x = 85
    result = fibonacci_search(arr, x)
    print(f"Element {x} is at index: {result}")

    # For doctests, run: python3 -m doctest -v fibonacci_search.py
    # For manual testing, run: python3 fibonacci_search.py