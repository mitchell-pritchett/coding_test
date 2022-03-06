from typing import MutableSequence

def partition(a: MutableSequence) -> None:
    n = len(a)
    pl = 0
    pr = n-1
    x = a[n//2]

    while pl <= pr:
        while a[pl] < x:
            pl += 1
        while a[pr] > x:
            pr -= 1
        if pl <= pr: 
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1
    print('pivot is', x)
    print('under or equal to pivot:', a[0:pl])
    print('over or equal to pivot:', a[pr+1:])
    print('eqaul to pivot:', a[pr+1:pl])

if __name__ == '__main__':
    a = [1,8,7,4,5,2,6,3,9]
    print(a)
    partition(a)
        