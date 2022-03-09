import heapq

from typing import MutableSequence

def heap_sort(a: MutableSequence) -> None:
    heap = []
    for i in a:
        heapq.heappush(heap, i) # min heap 임! 가장 작은 게 루트 노드
    for i in range(len(a)):
        a[i] = heapq.heappop(heap) # 루트 팝하고 다시 힙 만들고

if __name__ == "__main__":
    print("heap sort")
    x = [6,4,3,7,1,9,8]
    print('pre-sorting:', x)
    heap_sort(x)
    print('post-sorting:', x)

