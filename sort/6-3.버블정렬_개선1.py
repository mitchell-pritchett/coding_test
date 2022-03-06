from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    '''bubble sort improved 1: after no exchange pass stop!'''
    ccnt = 0
    scnt = 0
    n = len(a)
    for i in range(n-1):
        exchange_count_per_pass = 0
        for j in range(n-1, i, -1):
            ccnt += 1
            if a[j-1] > a[j]: 
                scnt += 1
                exchange_count_per_pass += 1
                a[j-1], a[j] = a[j], a[j-1]
        if not exchange_count_per_pass:
            break
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
