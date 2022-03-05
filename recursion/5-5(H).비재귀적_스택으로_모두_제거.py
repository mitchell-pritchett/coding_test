from stack import Stack

def recur(n: int) -> int:
    s = Stack(n)
    while True:
        if n > 0:
            s.push(n)
            n -= 1
            continue
        if not s.is_empty():
            n = s.pop()
            print(n)
            n -= 2
            continue


x = int(input('input integer: '))

recur(x)
