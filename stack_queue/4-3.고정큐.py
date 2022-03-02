from re import I
from typing import Any

class FixedQueue:
    class Empty(Exception):
        pass
    class Full(Exception):
        pass

    def __init__(self, maxlen: int) -> None:
        self.capacity = maxlen
        self.que = [None] * self.capacity
        self.front = 0
        self.rear = 0
        self.no = 0 # num of data
    
    def __len__(self) -> int:
        return self.no
    
    def is_empty(self) -> bool:
        return self.no <= 0
    
    def is_full(self) -> bool:
        return self.no >= self.capacity
    
    def enque(self, value: Any) -> None:
        if self.is_full(): raise FixedQueue.Full
        else:
            self.que[self.rear] = value
            self.rear += 1
            self.no += 1
        if self.rear == self.capacity:
            self.rear = 0
        
    def deque(self) -> Any:
        if self.is_empty(): raise FixedQueue.Empty
        else:
            x = self.que[self.front]
            self.front += 1
            self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return x

    def peek(self) -> Any:
        if self.is_empty(): raise FixedQueue.Empty
        else:
            return self.que[self.front]
    
    def find(self, value: Any) -> int:
        try: self.que.index(value)
        except: return -1
        # or 
        # for i, val in enumerate(self.que):
        #     if val == value: return i
        # return -1
        # or
        # for i in range(self.no):
        #     idx = (i + self.front) % self.capacity
        #     if self.que[idx] == value:
        #         return idx

    def count(self, value: Any) -> int:
        return self.que.count(value)
        # or
        # count = 0
        # for val in self.que:
        #    if val == value:
        #       count += 1

    def __contains__(self, value: Any) -> bool:
        return self.count(value) > 0
    
    def clear(self) -> None:
        self.front  = self.rear = self.no = 0
    
    def dump(self) -> None:
        if self.is_empty(): print('empty queue')
        else:
            for i in range(self.no):
                idx = (i + self.front) % self.capacity
                print(self.que[idx], end=' ')


    

    



