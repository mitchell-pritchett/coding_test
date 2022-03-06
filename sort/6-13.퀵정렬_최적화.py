from typing import MutableSequence, MutableSequence

def sort3(a: MutableSequence, idx1: int, idx2: int, idx3: int) -> int:
    if a[idx2] < a[idx1]: a[idx1], a[idx2] = a[idx2], a[idx1]
    if a[idx3] < a[idx2]: a[idx2], a[idx3] = a[idx3], a[idx2]
    if a[idx3] < a[idx1]: a[idx1], a[idx3] = a[idx3], a[idx1]
    return idx2

def insertion_sort(a: MutableSequence, left: int, right: int) -> None:
    for i in range(left+1, right+1):
        j = i
        tmp = a[i]
        while j > 0 and a[j-1] > tmp:
            a[j] = a[j-1]
            j -= 1
        a[j] = tmp

def qsort(a: MutableSequence, left: int, right: int) -> None:
    if right - left < 9:
        insertion_sort(a, left, right)
    else:
        pl = left
        pr = right
        m = sort3(a, pl, (pl+pr)//2, pr)
        x = a[m]

        a[m], a[pr-1] = a[pr-1], a[m]
        pl += 1
        pr -= 2
        while pl <= pr:
            while a[pl] < x: pl += 1
            while a[pr] > x: pr += 1
            if pl <= pr:
                a[pl], a[pr] = a[pr], a[pl]
                pl += 1
                pr -= 1
        if left < pr: qsort(a, left, pr)
        if pl < right: qsort(a, pl, right)

def quick_sort(a: MutableSequence) -> None:
    qsort(a, 0, len(a)-1)

if __name__ == '__main__':
    a = [5,8,4,2,6,1,3,9,7]
    print('before quick sort:')
    print(a)
    quick_sort(a)
    print('after quick sort(or insertion sort under 9 elements):')
    print(a)
