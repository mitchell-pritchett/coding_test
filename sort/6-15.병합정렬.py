from typing import MutableSequence

def merge_sort(a: MutableSequence) -> None:

    def _merge_sort(a: MutableSequence, left: int, right: int) -> None:
        if left < right:
            print('buff:', buff)
            print(a)
            center = (left + right) // 2

            _merge_sort(a, left, center)
            _merge_sort(a, center+1, right)
            # 정렬이 되고 나면
            p = j = 0
            i = k = left

            while i <= center: # left buff에 복사
                buff[p] = a[i]
                p += 1
                i += 1
            
            while i <= right and j < p: # i는 center에서 right 까지, j는 0에서 센터 전까지
                if buff[j] <= a[i]:
                    a[k] = buff[j]
                    j += 1
                else:
                    a[k] = a[i]
                    i += 1
                k += 1

            while j < p: # 우측은 이미 정렬되어서 a에 있으니 남은 왼쪽만 정리해주면 된다.
                a[k] = buff[j]
                k += 1
                j += 1
    
    n = len(a)
    buff = [None] * n
    _merge_sort(a, 0, n-1)
    del buff

if __name__ == '__main__':
    a = [5,4,3,2,1]
    merge_sort(a)
    print('final:', a)