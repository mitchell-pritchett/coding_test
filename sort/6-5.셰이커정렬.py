from typing import MutableSequence

def shaker_sort(a: MutableSequence) -> None:
    ccnt = 0
    scnt = 0

    left = 0
    right = len(a) - 1
    last = right
    while left < right:
        for j in range(right, left, -1):
            ccnt += 1
            if a[j-1] > a[j]:
                scnt += 1
                a[j-1], a[j] = a[j], a[j-1]
                last = j
        left = last

        for j in range(left, right):
            ccnt += 1
            if a[j] > a[j+1]:
                scnt += 1
                a[j], a[j+1] = a[j+1], a[j]
                last = j
        right = last

    print('total compare count:', ccnt)
    print('total exchange count:', scnt)

if __name__ == '__main__':
    print('shaker sort')
    num = int(input('input number of elements: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
    
    shaker_sort(x)
    print("sorted:", x)