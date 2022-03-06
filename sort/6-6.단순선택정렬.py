from typing import MutableSequence

def selection_sort(a: MutableSequence) -> None:
    n = len(a)

    for i in range(n):
        min = i # min = a[i] 로 잡지 않고 인덱스로 잡는 게 포인트!
        for j in range(i+1, n):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]

if __name__ == '__main__':
    print('-' * 30)
    print('selection sort')
    num = int(input('input number of elements: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
    
    selection_sort(x)
    print("sorted:", x)
