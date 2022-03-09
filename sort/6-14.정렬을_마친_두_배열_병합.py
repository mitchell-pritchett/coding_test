'''
merge sort
a : list
b: list
c : list
c에 작은 것을 대입하는 방식으로 반복하고,
pa, pb는 대입된 경우에만 이동하고 그렇지 않은 애는 그대로 있는다. pc는 매번 이동.
그리고 종료 조건은 pc가 a와 b의 길이의 합에 해당하는 인덱스에 도착했을 때
'''
from typing import MutableSequence, Sequence

def merge_sorted_list(a: Sequence, b: Sequence) -> MutableSequence:
    pa = pb = pc = 0 # pointer init
    na = len(a)
    nb = len(b)
    n = na + nb
    c = [None] * n

    while pa < na and pb < nb: # 둘이 공존하는 경우에까지 쭉 돌리고
        print(c)
        print(f'쭉 pa:{pa}, pb:{pb}, pc:{pc}')
        if a[pa] < b[pb]:
                x = a[pa]
                pa += 1
        else:
            x = b[pb]
            pb += 1
        c[pc] = x
        pc += 1
    
    while pb < nb:
            c[pc] = b[pb]
            pb += 1
            pc += 1

    while pa < na:
            c[pc] = a[pa]
            pa += 1
            pc += 1
            
    return c

if __name__ == '__main__':
    x = merge_sorted_list([2,4,6,8,11,13], [1,2,3,4,9,16,21])
    print('-'*30)
    print(x)

    

