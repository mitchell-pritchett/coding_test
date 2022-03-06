from re import A
from typing import MutableSequence

def shell_sort(a: MutableSequence) -> None:
    n = len(a)
    h = 1

    while h < n//9:
        h = h * 3 + 1
    
    while h > 0:
        for i in range(h, n):
            j = i - h
            tmp = a[i]
            while j >= 0 and a[j] > tmp:
                a[j + h] = a[j]
                j -= h
            a[j+h] = tmp # tmp 보다 작은 애 위치가 j니까 tmp는 j+h에 삽입
        h //= 3

if __name__ == '__main__':
    a = [1,4,5,2,6,2,6,1]
    print(a)
    shell_sort(a)
    print(a)
