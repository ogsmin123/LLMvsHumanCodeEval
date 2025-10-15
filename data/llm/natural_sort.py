import re
from typing import List

def natural_sort(strings: List[str]) -> List[str]:
    """
    Sorts a list of strings using natural sort order.
    
    Natural sort order is a way of sorting strings that takes into account
    human perception of numerical order within strings. For example, "file10"
    should come after "file2" when sorted naturally.
    
    Args:
    - strings: A list of strings to be sorted.
    
    Returns:
    - A new list of strings sorted in natural order.
    """
    
    def alphanum_key(s: str):
        """
        Convert a string into a list of strings and integers that represent
        the natural sort order.
        
        This function splits the string into a list where each element is
        either an integer or a non-numeric string. This allows for comparison
        that respects numeric order within the string.
        
        Args:
        - s: The string to be converted.
        
        Returns:
        - A list of strings and integers.
        """
        # Use regular expression to split the string into parts
        # \d+ matches sequences of digits
        # \D+ matches sequences of non-digits
        return [int(text) if text.isdigit() else text.lower() for text in re.split('(\d+)', s)]
    
    # Sort using the alphanum_key function as the key
    return sorted(strings, key=alphanum_key)

# Example usage:
# sorted_list = natural_sort(["file10", "file2", "file1"])
# print(sorted_list)  # Output: ['file1', 'file2', 'file10']