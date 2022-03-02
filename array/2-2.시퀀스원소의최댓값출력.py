<<<<<<< HEAD
from typing import Sequence, Any

def max_of(s: Sequence) -> Any:
    maximum = s[0]
    for i in range(1,len(s)):
        if s[i] > maximum : maximum = s[i]
    return maximum
    
    # for i in s[1:]:
    #     if i > maximum: maximum = i
    # return maximum

if __name__ == '__main__':
    print("배열의 최댓값을 구합니다.")
    num = int(input('원소의 수를 입력하세요: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f"x[{i}]값을 입력하세요: "))
=======
from typing import Sequence, Any

def max_of(s: Sequence) -> Any:
    maximum = s[0]
    for i in range(1,len(s)):
        if s[i] > maximum : maximum = s[i]
    return maximum
    
    # for i in s[1:]:
    #     if i > maximum: maximum = i
    # return maximum

if __name__ == '__main__':
    print("배열의 최댓값을 구합니다.")
    num = int(input('원소의 수를 입력하세요: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f"x[{i}]값을 입력하세요: "))
>>>>>>> 2d8319d170ef6f026fca7327b39a71e5297cfca9
    print("최댓값은", max_of(x))