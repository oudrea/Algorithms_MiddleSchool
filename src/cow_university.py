from utils.utils import read_number_array


def maximum_position(A: list[int], start: int, end: int) -> int:
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
    cow = read_number_array("Please enter your array:")
    cow = selection_sort_array(cow, len(cow))
    print(f"The sorted array is {cow}")
    best_cow_pos = 0
    for i in range(len(cow)):
        p = (len(cow) - i) * cow[i]
        best_profit_up_to_now = (len(cow) - best_cow_pos) * cow[best_cow_pos]
        if p > best_profit_up_to_now:
            best_cow_pos=i
    print(f"Best profit is {(len(cow) - best_cow_pos) * cow[best_cow_pos]}, with a price of {cow[best_cow_pos]}")