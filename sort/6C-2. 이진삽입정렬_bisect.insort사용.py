from typing import MutableSequence
import bisect

def binary_insertion_sort(a: MutableSequence) -> None:
    for i in range(1, len(a)):
        bisect.insort(a, a.pop(i), 0, i)
        print(a)
        # insort(a, x, lo, hi) : a가 이미 정렬된 상태를 유지하면서, a[lo]~a[hi] 사이에 x를 삽입. x와 같은 값이 여러개 있으면 가장 오른쪽에 삽입.

if __name__ == '__main__': binary_insertion_sort([3,5,2,5,1,3,4,6])