from utils.utils import read_number

def is_prime(number: int) -> bool:
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for x in range(3, number // 2, 2):
        if number % x == 0:
            return False
    return True


if __name__ == '__main__':
    number = read_number('Please enter your number:')
    is_number_prime = is_prime(number)
    print(f"Number {number} {'is' if is_number_prime else 'is not'} prime.")