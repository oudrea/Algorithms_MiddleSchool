
from utils.utils import print_array, read_number_array


if __name__ == '__main__':
    numbers = read_number_array('Please provide your array of numbers:')
    changed = True
    iteration = 1
    comparisons = 0
    while changed:
        changed = False
        for i in range(len(numbers) - 1):
            comparisons = comparisons + 1
            if numbers[i] > numbers[i + 1]:
                temp = numbers[i]
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = temp
                changed = True
        print_array(f"After iteration {iteration} and {comparisons} comparisons array is", numbers)
        iteration = iteration + 1
    print_array("Final sorted array is", numbers)