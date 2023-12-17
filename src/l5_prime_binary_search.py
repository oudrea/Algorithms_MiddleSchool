from l1_binary_search import binary_search
from utils.utils import read_number, read_number_array_file


if __name__ == '__main__':
    primes = read_number_array_file('primes.txt')
    number = read_number('Please enter your number:')
    is_prime = binary_search(primes, number, 0, len(primes)) >= 0
    print(f"Number {number} {'is' if is_prime else 'is not'} prime.")
    