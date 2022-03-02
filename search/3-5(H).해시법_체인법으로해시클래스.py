<<<<<<< HEAD
from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:
    def __init__(self, key: Any, value: Any, next: Node) -> None:
        self.key = key
        self.value = value # hash_value
        self.next = next # next_node

class ChainedHash:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity # 해시테이블 크기
        self.table = [None] * self.capacity

    def hash_value(self, key: Any) -> int:
        if isinstance(key, int): # key가 int면 그냥 나눠서 해시값을 구하고
            return key % self.capacity
        return int(hashlib.sha256(str(key).encode()).hexdigest(), 16) / self.capacity
        # str(key).encode(); sha256 알고리즘은 바이트 문자열만 인수로 받으므로 문자열로 바꾼다음 다시 인코딩으로 바이트로 바꿔줌. 
        # .hexdigest(); sha256이 리턴하는 생성자에서 해시값을 16진수 문자열로 꺼내고
        # int(<16진수문자열>, 16); 10진수 정수로 바꿔줌
        # / self.capacity 이거를 우리가 설정한 해시 테이블 길이로 나눠줘서 우리 해시 테이블에 맞는 해시값을 리턴
    
    def search(self, key: Any) -> Any:
        hash_value = self.hash_value(key)
        p = self.table[hash_value] # 첫 노드
        while p is not None: # 뭔가 있으면 일단 가서 , 다음으로 간 곳이 None이면 그만하고 아래로 가서 return None
            if p.key == key: # 그 값이랑 같니?
                return p.value # 같으면 리턴
            p = p.next # 다르니 그럼 다음 노드
        return None
    
    def add(self, key: Any, value: Any) -> bool: # 추가 성공 실패 여부
        if self.search(key): return False
        # 검색해보니까 없다
        hash_value = self.hash_value(key)
        p = self.table[hash_value]

        while p is not None:
            p = p.next
        # p가 None이다.
        # 여기에 제일 앞에 넣어준다.
        self.table[hash_value] = Node(key, value, self.table[hash_value])
        return True
    
    def add_book(self, key: Any) -> bool:
        hash_value = self.hash_value(key)
        p = self.table[hash_value]

        while p is not None:
            if p.key == key: 
                return False # already exists
            p = p.next
        
        self.table[hash_value] = Node(key, hash_value, self.table[hash_value])
        return True
    
    def remove(self, key: Any) -> bool:
        hash_value = self.hash_value(key)
        p = self.table[hash_value]
        pp = None

        while p is not None:
            if p.key == key:
                if pp is None:
                    self.table[hash_value] = p.next
                else: pp.next = p.next
                return True
            # 그 p가 아니야
            pp = p
            p = p.next
        return False # p가 None
        
    def dump(self) -> None: # 해시 테이블 전체를 출력
        for i in range(self.capacity):
            print(f"{i:>2}", end='')
            p = self.table[i]
            while p is not None:
                print(f"  -> {p.key:>2}({p.value})", end='')
                p = p.next
            print()

##########################################################################
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

hash = ChainedHash(13)

while True:
    menu = select_menu()

    if menu == Menu.add:
        key = int(input('key to add: '))
        value = input('value to add: ')
        if hash.add(key, value) is False:
            print("adding failed")
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







=======
from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:
    def __init__(self, key: Any, value: Any, next: Node) -> None:
        self.key = key
        self.value = value # hash_value
        self.next = next # next_node

class ChainedHash:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity # 해시테이블 크기
        self.table = [None] * self.capacity

    def hash_value(self, key: Any) -> int:
        if isinstance(key, int): # key가 int면 그냥 나눠서 해시값을 구하고
            return key % self.capacity
        return int(hashlib.sha256(str(key).encode()).hexdigest(), 16) / self.capacity
        # str(key).encode(); sha256 알고리즘은 바이트 문자열만 인수로 받으므로 문자열로 바꾼다음 다시 인코딩으로 바이트로 바꿔줌. 
        # .hexdigest(); sha256이 리턴하는 생성자에서 해시값을 16진수 문자열로 꺼내고
        # int(<16진수문자열>, 16); 10진수 정수로 바꿔줌
        # / self.capacity 이거를 우리가 설정한 해시 테이블 길이로 나눠줘서 우리 해시 테이블에 맞는 해시값을 리턴
    
    def search(self, key: Any) -> Any:
        hash_value = self.hash_value(key)
        p = self.table[hash_value] # 첫 노드
        while p is not None: # 뭔가 있으면 일단 가서 , 다음으로 간 곳이 None이면 그만하고 아래로 가서 return None
            if p.key == key: # 그 값이랑 같니?
                return p.value # 같으면 리턴
            p = p.next # 다르니 그럼 다음 노드
        return None
    
    def add(self, key: Any, value: Any) -> bool: # 추가 성공 실패 여부
        if self.search(key): return False
        # 검색해보니까 없다
        hash_value = self.hash_value(key)
        p = self.table[hash_value]

        while p is not None:
            p = p.next
        # p가 None이다.
        # 여기에 제일 앞에 넣어준다.
        self.table[hash_value] = Node(key, value, self.table[hash_value])
        return True
    
    def add_book(self, key: Any) -> bool:
        hash_value = self.hash_value(key)
        p = self.table[hash_value]

        while p is not None:
            if p.key == key: 
                return False # already exists
            p = p.next
        
        self.table[hash_value] = Node(key, hash_value, self.table[hash_value])
        return True
    
    def remove(self, key: Any) -> bool:
        hash_value = self.hash_value(key)
        p = self.table[hash_value]
        pp = None

        while p is not None:
            if p.key == key:
                if pp is None:
                    self.table[hash_value] = p.next
                else: pp.next = p.next
                return True
            # 그 p가 아니야
            pp = p
            p = p.next
        return False # p가 None
        
    def dump(self) -> None: # 해시 테이블 전체를 출력
        for i in range(self.capacity):
            print(f"{i:>2}", end='')
            p = self.table[i]
            while p is not None:
                print(f"  -> {p.key:>2}({p.value})", end='')
                p = p.next
            print()

##########################################################################
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

hash = ChainedHash(13)

while True:
    menu = select_menu()

    if menu == Menu.add:
        key = int(input('key to add: '))
        value = input('value to add: ')
        if hash.add(key, value) is False:
            print("adding failed")
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







>>>>>>> 2d8319d170ef6f026fca7327b39a71e5297cfca9
