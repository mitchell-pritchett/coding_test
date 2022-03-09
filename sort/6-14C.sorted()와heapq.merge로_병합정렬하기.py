a = [1,2,3,4]
b = [3,5,7,9,11,13]
c = list(sorted(a + b)) # 속도가 빠르지 않다. 굳이 a,b가 정렬되어있을 필요도 없고.


import heapq

c = list(heapq.merge(a, b)) 
print("heapq.merge(a,b)", c)