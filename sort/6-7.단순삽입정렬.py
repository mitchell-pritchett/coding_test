'''
단순삽입정렬은 두 번째 원소부터 주목하면서 시작한다. 총 n-1 번의 패스.
주목한 원소보다 더 앞쪽에서 알맞은 위치로 삽입하며 정렬.

그러니까 단계는
1. 아직 정렬되지 않은 부분의 맨 앞 원소에 주목한다. 이를 tmp에 넣어놓고 앞부분들이랑 비교를 한다.
2. 주목한 원소보다 더 앞쪽에서 알맞은 위치로 삽입한다. 근데 어떻게 알맞은 위치를 찾는가?
    2-1. 예를 들어 주목한 숫자가 3이면 그 숫자보다 작은 숫자를 찾을때까지 앞쪽 애들이랑 비교를 해서
    2-2. 3보다 크면 3 자리에 그 큰 애를 넣는다. 이걸 하나씩 앞으로 가면서 반복한다. 3보다 작은 애를 찾기 전까지는 3은 이용하지 않는다.
    2-3. 3보다 작은 애를 찾았다. 그러면 그 작은 애 뒷자리에 3을 넣는다.
    2-4. 1로 돌아간다.
'''
from typing import MutableSequence

def insertion_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(1, n): # 1~n-1까지 하나씩 뒤로 가며 n-1번 반복
        tmp = a[i]
        for j in range(i-1,-2,-1):
            print(a) # i 전까지 애들이랑 tmp 비교
            if a[j] < tmp or j < 0:
                a[j+1] = tmp
                break
            else:
                a[j+1] = a[j]
            
def insertion_sort_book(a: MutableSequence) -> None:
    n = len(a)
    for i in range(1, n):
        j = i # key!
        tmp = a[i]
        while j > 0 and a[j-1] > tmp:
            a[j] = a[j-1]
            j -= 1
        a[j] = tmp


if __name__ == '__main__':
    print('insertion sort')
    num = int(input('input number of elements: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
    
    insertion_sort(x)
    print("sorted:", x)

