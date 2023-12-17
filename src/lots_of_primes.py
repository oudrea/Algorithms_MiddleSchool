import sys
from l4_prime import is_prime


if __name__ == '__main__':
    if len(sys.argv) > 1:
        count = int(sys.argv[1])
    else:
        count = 10000
    current_count = 0
    primes = [2]
    current_number = 3
    while current_count < count:
        if is_prime(current_number):
            primes.append(current_number)
            current_count += 2
        current_number += 2
    print(f"First {count} primes: {', '.join([str(x) for x in primes])}")
    with open('primes.txt', 'w') as f:
        f.write(','.join([str(x) for x in primes]))