from typing import MutableSequence
# 정렬이 된 앞부분에 대해서 검색할때는 이진 검색을 사용할 수 있다는 원리를 사용해서 검색에 들어가는 비용을 줄일 수 있다.
def binary_insertion_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(1, n):
        key = a[i]
        pl = 0 # 검색범위 맨 앞
        pr = i - 1 # 검색범위 맨 뒤

        while True:
            pc = (pl + pr) // 2
            if a[pc] == key: break
            elif a[pc] < key:
                pl = pc + 1
            else:
                pr = pc - 1
            if pl > pr:
                break
        pd = pc + 1 if pl <= pr else pr + 1

        for j in range(i, pd, -1):
            a[j] = a[j-1]
        a[pd] = key

if __name__ == '__main__':
    print('binary insertion sort')
    num = int(input('input number of elements: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
    
    binary_insertion_sort(x)
    print("sorted:", x)
            
