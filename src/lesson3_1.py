from utils.utils import read_number_array


def maximum_position(a: list[int], start: int, end: int) -> int:
    max_pos_to_now = start
    for i in range(start, end):
        if A[max_pos_to_now] < A[i]:
            max_pos_to_now = i
    return max_pos_to_now


def selection_sort_array(A: list[int], e: int):
    for end in range(e, 1 , -1):
        max_pos=maximum_position(A,0,end)
        temp=A[end-1]
        A[end-1]=A[max_pos]
        A[max_pos]=temp
    return A


if __name__ == '__main__':
    A = read_number_array("Please enter your array:")
    A = selection_sort_array(A, len(A))
    print(f"The sorted array is {A}")
    