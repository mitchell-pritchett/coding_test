def move(no: int, x: int, y: int) -> None:
    '''move no plates from x tower to y tower'''
    '''total of three towers by default'''
    if no > 1: # stage 1
        move(no-1, x, 6 - x - y)
    
    print(f'move plate[{no}] from tower {x} to tower {y}') # stage 2

    if no > 1: # stage 3
        move(no-1, 6 - x - y, y)

print('towers of hanoi')
n = int(input('input number of plates: '))

move(n, 1, 3)


