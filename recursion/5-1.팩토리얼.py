import math

def factorial(n: int) -> int:
    if n > 0:
        return n * factorial(n-1)
    elif n == 0:
        return 1
    else:
        raise ValueError

if __name__ == '__main__':
    n = int(input('input: '))
    print(factorial(n))
    # math.factorial
    print(math.factorial(n))