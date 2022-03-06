from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    ccnt = 0
    scnt = 0
    n = len(a)
    k = 0
    while k < n-1:
        last = n-1
        for j in range(n-1, k, -1):
            ccnt += 1
            if a[j-1] > a[j]:
                scnt += 1
                a[j-1], a[j] = a[j], a[j-1]
                last = j
        k = last
    print('total compare count:', ccnt)
    print('total exchange count:', scnt)

if __name__ == '__main__':
    print('bubble sort')
    num = int(input('input number of elements: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
    
    bubble_sort(x)
    print("sorted:", x)