

import math
from utils.utils import read_number, read_number_array

## TODO: THIS IS WHERE WE IMPLEMENT BINARY SEARCH
##    This function should try to find the number in the array
##    between positions [start,end)
##    assuming the array is sorted
##    It should return the position where the number is found, or -1 if not found
def binary_search(sorted_array: list[int], number: int, start: int, end: int) -> int:
    if start == end - 1:
        if sorted_array[start] == number:
            return start
        else: return -1
    else:
        middle = math.floor((start + end) / 2)
        if number < sorted_array[middle]:
            return binary_search(sorted_array, number, start, middle - 1)
        elif number > sorted_array[middle]:
            return binary_search(sorted_array, number, middle + 1, end)
        else: return middle 


if __name__ == '__main__':
    numbers = read_number_array('Enter your sorted array of numbers:')
    number_to_search = read_number('Enter the number to search for:')
    position_found = binary_search(numbers, number_to_search, 0, len(numbers))
    if position_found >= 0:
        print(f"Number {number_to_search} found at position {position_found}")
    else:
        print(f"Number {number_to_search} not found")
