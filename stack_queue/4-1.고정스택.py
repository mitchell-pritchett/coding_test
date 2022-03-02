from typing import Any

class FixedStack:
    class Empty(Exception):
        pass
    class Full(Exception):
        pass

    def __init__(self, capacity: init = 256) -> None:
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0
    
    def __len__(self) -> int: # __len__()를 정의하면 클래스형의 인스턴스를 len() 함수에 전달할 수 있다. len(class_obj) 이런 식으로
        return self.ptr
    
    def is_empty(self) -> bool:
        return self.ptr <= 0 
    
    def is_full(self) -> bool:
        return self.ptr >= self.capacity

    def push(self, value: Any) -> None:
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]
    
    def peek(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[self.ptr -1]
    
    def clear(self) -> None:
        self.ptr = 0
    
    def find(self, value: Any) -> int:
        '''top to bottom find value and return the first found index'''
        if self.is_empty():
            raise FixedStack.Empty
        for i in range(self.ptr-1, -1, -1):
            if self.stk[i] == value:
                return i
        return -1    

    def count(self, value: Any) -> int:
        counter = 0
        for i in range(self.ptr-1, -1, -1):
            if self.stk[i] == value:
                counter += 1
        return counter 

    def __contains__(self, value: Any) -> bool: # __contains__() 함수를 정의하면 클래스형의 인스턴스에 맴버십 판단 연산자 in을 적용할 수 있다.
        return self.count(value) > 0
    
    def dump(self) -> None:
        if self.is_empty():
            print('empty stack')
        print(self.stk[:self.ptr])
