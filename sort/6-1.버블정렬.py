from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    ccnt = 0 # compare count
    scnt = 0 # exchange count
    n = len(a)
    for i in range(n-1):
        for j in range(n-1, i, -1):
            ccnt += 1
            if a[j - 1] > a[j]:
                scnt += 1
                a[j - 1], a[j] = a[j], a[j - 1]
        print(f'pass {i+1}')
        print(a)
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
