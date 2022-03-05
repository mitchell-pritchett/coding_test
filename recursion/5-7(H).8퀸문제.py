from stat import FILE_ATTRIBUTE_INTEGRITY_STREAM


pos = [0] * 8 # 각 열에서의 위치
flag_a = [False] * 8 # 행의 배치 여부
flag_b = [False] * 15 # 오른쪽 대각선 배치 여부
flag_c = [False] * 15 # 왼쪽 대각선 배치 여부

def put() -> None:
    '''각 열에 배치된 퀸의 위치를 출력'''
    for j in range(8):
        for i in range(8):
            print('[O]' if pos[i] == j else '[X]', end='')
    print()

def set(i: int) -> None:
    '''i열에 퀸 배치'''
    for j in range(8):
        if (not flag_a[j] and not flag_b[i + j] and not flag_c[7 + i - j]):
            pos[i] = j
            if i == 7:
                put()
            else:
                flag_a[j] = flag_b[i+j] = flag_c[7+i-j] = True
                set(i + 1) # 다음 열에 퀸을 배치
                flag_a[j] = flag_b[i+j] = flag_c[7+i-j] = False

set(0)