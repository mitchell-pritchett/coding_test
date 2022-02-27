from typing import Sequence, Any
import copy

def seq_search(seq: Sequence, key: Any) -> int:
    # seq=[1,2,3], key=5
    seq_copy = copy.deepcopy(seq) # deepcopy()를 해야 바꿔도 영향 없음

    seq_copy.append(key) # seq_copy=[1,2,3,5]
    for i in range(len(seq_copy)):
        if seq_copy[i] == key:
            break
    return (i if i != len(seq) else None)

if __name__ == '__main__':
    l = []
    n = int(input('원소 수를 입력하세요: '))
    for i in range(n):
        l.append(int(input(f'x[{i}]: ')))
    k = int(input('검색할 값을 입력하세요: '))
    print(f'검색값은 x[{seq_search(l, k)}]에 있습니다.' if seq_search(l,k) else '검색값이 데이터에 없습니다.')

