<<<<<<< HEAD
def card_conv(x: int, r: int) -> str: # 리턴을 스트링으로 해야함!
    d = ''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ' # 뽀인투!

    n = len(str(x))
    print(f"{r:2} | {x:{n}d}") # 정렬 외우기!
    while x > 0:
        print("   +" + "-" * (n+2))
        d = dchar[x % r] + d # 뽀인투!
        print(f"{r:2} | {x // r:{n}d} ... {x % r}")
        x //= r
    return d

if __name__ == '__main__':
    print("10진수를 n진수로 변환합니다.")

    while True:
        while True: 
            n = int(input('변환할 값으로 음이 아닌 정수를 입력하세요: '))
            if n > 0: break
        
        while True:
            r = int(input('어떤 진수로 변환할까요: '))
            if (2 <= r <= 36):
                break       

        print(f"{r}진수로는 {card_conv(n, r)}입니다.")

        if input('한 번 더 변환할까요? Y는 예, N은 아니오: ') ==  'N':
            break

=======
def card_conv(x: int, r: int) -> str: # 리턴을 스트링으로 해야함!
    d = ''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ' # 뽀인투!

    n = len(str(x))
    print(f"{r:2} | {x:{n}d}") # 정렬 외우기!
    while x > 0:
        print("   +" + "-" * (n+2))
        d = dchar[x % r] + d # 뽀인투!
        print(f"{r:2} | {x // r:{n}d} ... {x % r}")
        x //= r
    return d

if __name__ == '__main__':
    print("10진수를 n진수로 변환합니다.")

    while True:
        while True: 
            n = int(input('변환할 값으로 음이 아닌 정수를 입력하세요: '))
            if n > 0: break
        
        while True:
            r = int(input('어떤 진수로 변환할까요: '))
            if (2 <= r <= 36):
                break       

        print(f"{r}진수로는 {card_conv(n, r)}입니다.")

        if input('한 번 더 변환할까요? Y는 예, N은 아니오: ') ==  'N':
            break

>>>>>>> 2d8319d170ef6f026fca7327b39a71e5297cfca9
