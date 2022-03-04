import math

def gcd(x: int, y: int) -> int:
    if y == 0:
        return x
    return gcd(y, x%y)

if __name__ == '__main__':
    print("calculating gcd of two integers.")
    x = int(input("first integer: "))
    y = int(input("second integer: "))
    if x < y: x, y = y, x
    print(f"GCD of {x} and {y} is {gcd(x,y)}")
    print(f'math.gcd({x},{y}) result: {math.gcd(x,y)}')
