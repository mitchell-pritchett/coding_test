from typing import MutableSequence

def heap_sort(a: MutableSequence) -> None:

    def down_heap(a: MutableSequence, left: int, right: int) -> None:
        temp = a[left]

        parent = left
        while parent < (right + 1) // 2: # parent의 위치 마지막은 말단 노드의 부모 노드 위치까지
            cl = parent * 2 + 1
            cr = cl + 1
            child = cr if cr <= right and a[cr] > a[cl] else cl # 오른쪽 자식이 있는 경우 비교하고, 더 큰 값을 선택
            if temp >= a[child]: # parent 값이 더 크면 break
                break
            a[parent] = a[child] # parent 자리에 child 값을 넣고
            parent = child # parent index 에 child의 인덱스를 넣는다. 그럼 parent의 위치가 아래로 하나 이동
        # parent의 이동이 다 끝나면 그 위치에 temp로 맡아뒀던 parent 값을 넣는다.
        a[parent] = temp
    
    n = len(a)

    for i in range((n-1)//2, -1, -1): # 말단 노드의 부모 인덱스부터 시작해서 하나씩 앞으로 이동
        down_heap(a, i, n-1) # 제일 아래 서브 트리부터 해서, 루트 노드까지 이동해서 힙으로 만든다.
    
    # 힙으로 만들었으면, 말단 노드와 루트 노드를 교환하고 정렬 안된 부분에서 또 정렬하고 하는 방식을 반복
    for i in range(n-1, 0, -1):
        a[0], a[i] = a[i], a[0]
        down_heap(a, 0, i-1)

if __name__ == "__main__":
    print("heap sort")
    x = [6,4,3,7,1,9,8]
    print('pre-sorting:', x)
    heap_sort(x)
    print('post-sorting:', x)



