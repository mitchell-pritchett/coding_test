from __future__ import annotations
from typing import Any, Type
from enum import Enum
import hashlib

# 버킷 속성
class Status(Enum):
    OCCUPIED = 0
    EMPTY = 1
    DELETED = 2

class Bucket:
    '''해시를 구성하는 버킷'''
    def __init__(self, key: Any = None, value: Any = None, stat: Status = Status.EMPTY) -> None:
        self.key = key
        self.value = value
        self.stat = stat
    
    def set(self, key: Any, value: Any, stat: Status) -> None:
        self.key = key
        self.value = value
        self.stat = stat
    
    def set_status(self, stat: Status) -> None:
        self.stat = stat
    
class OpenHash:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.table = [Bucket()] * self.capacity
    
    def hash_value(self, key: Any) -> int:
        if isinstance(key, int):
            return key % self.capacity
        return int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity
    
    def rehash_value(self, key: Any) -> int:
        return (self.hash_value(key) + 1) % self.capacity # 예를 들어 13 넘어가면 안되니까 나줘준다
    
    def search_node(self, key:Any) -> Any: # bucket 리턴
        hash_value = self.hash_value(key)
        p = self.table[hash_value]

        for _ in range(self.capacity):
            if p.stat == Status.EMPTY:
                break
            elif p.key == key:
                return p
            rehash_value = self.rehash_value(key)  
            p = self.table[rehash_value]
        return None
    
    def search(self, key:Any) -> Any:
        p = self.search_node(key)
        return p.value if p else None
    
    def add(self, key: Any, value: Any) -> bool:
        if self.search_node(key) is None: # doesn't exist
            hash_value = self.hash_value(key)
            for _ in range(self.capacity):
                p = self.table[hash_value]
                if p.stat == Status.EMPTY or p.stat == Status.DELETED:
                    self.table[hash_value] = Bucket(key, value, Status.OCCUPIED)
                    return True
                hash_value = self.rehash_value(hash_value)
        return False

    def remove(self, key: Any) -> bool:
        p = self.search_node(key)
        if  p is None: print('검색했는데 없다'); return False # 검색해보니 없다.
        print('검색해보니 있다')
        p.set_status(Status.DELETED)
        print('그래서 지웠다.')
        return True
    
    def dump(self) -> None:
        for i, p in enumerate(self.table):
            print((i, p.key, p.value, p.stat) if p.stat == Status.OCCUPIED else f'{i} 미등록')

######################################################################
from enum import Enum
# from chained_hash import ChainedHash

Menu = Enum('Menu', ['add','remove','search','dump', 'end'])

def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='  ', end='')
        n = int(input(": "))
        if 1 <= n <= len(Menu):
            return Menu(n)

hash = OpenHash(13)

while True:
    menu = select_menu()

    if menu == Menu.add:
        key = int(input('key to add: '))
        value = input('value to add: ')
        if hash.add(key, value) is False:
            print("adding failed, table full")

    elif menu == Menu.remove:
        key = int(input('key to delete: '))
        if hash.remove(key) is False:
            print('removing failed')

    elif menu == Menu.search:
        key = int(input('key to search: '))
        if hash.search(key) is None:
            print('search failed')

        else: print(f'found value: {hash.search(key)}')
        
    elif menu == Menu.dump:
        hash.dump()

    else:
        break