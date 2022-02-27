from typing import Sequence, Any

def seq_search(a: Sequence, key: Any) -> int:
    for i in range(len(a)):
        if a[i] == key:
            return i
    return None

if __name__ == '__main__':
    l = []
    n = int(input('원소 수를 입력하세요: '))
    for i in range(n):
        l.append(int(input(f'x[{i}]: ')))
    k = int(input('검색할 값을 입력하세요: '))
    print(f'검색값은 x[{seq_search(l, k)}]에 있습니다.' if seq_search(l,k) else '검색값이 데이터에 없습니다.')
