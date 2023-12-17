import math

from utils.utils import read_number_array, read_number_array_file

if __name__ == '__main__':
    A = read_number_array_file("C:\\Users\\octav\\OneDrive\\Desktop\\Algorithms_MiddleSchool\\primes.txt");
#    A = read_number_array("Please enter your array:")
#    B = ["a", "b", "cccc", "d", "alsdjlashdoqwiue", "emma", "sebi"]
#    C = [2.3, 2.1, 1.2, 4.5]
#    D = [{"name": "emma", "age": 11, "address": "Scarsdale"}, {"name": "Sebi", "age":11, "address": "Valhalla"}]
    max_up_to_now = A[0]
    for x in A:
        if max_up_to_now < x:
            max_up_to_now = x
        print(f"I'm at element {x}, max up to now is {max_up_to_now}")
    max_up_to_now = A[0]
    for i in range(len(A)):
        if max_up_to_now < A[i]:
            max_up_to_now = A[i]
        print(f"I'm at element index {i}, max up to now is {max_up_to_now}")
    print(f"Maximum of the array is {max_up_to_now}")