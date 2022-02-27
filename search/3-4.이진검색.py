from typing import Sequence, Any

def bin_search(seq: Sequence, key: Any) -> int:
    pl = 0
    pr = len(seq) -1
    pc = (pl + pr) // 2

    while True:
        if seq[pc] == key: return pc
        if pl == pr: return -1
        if seq[pc] < key:
            pl = pc+1
            pc = (pl + pr)  // 2
        else:
            pr = pc-1
            pc = (pl + pr) // 2

# better 코드
def bin_search_book(seq: Sequence, key: Any) -> int:
    pl = 0
    pr = len(seq) -1

    while True:
        pc = (pl + pr) // 2
        if seq[pc] == key: return pc
        if pl == pr: return -1
        if seq[pc] < key:
            pl = pc+1
        else:
            pr = pc-1

if __name__ == '__main__':
    l = []
    n = int(input('원소 수를 입력하세요: '))
    print('데이터를 오름차순으로 입력하세요.')
    for i in range(n):
        l.append(int(input(f'x[{i}]: ')))
    k = int(input('검색할 값을 입력하세요: '))
    print(f'검색값은 x[{bin_search_book(l, k)}]에 있습니다.' if bin_search_book(l,k) != -1 else '검색값이 데이터에 없습니다.')

