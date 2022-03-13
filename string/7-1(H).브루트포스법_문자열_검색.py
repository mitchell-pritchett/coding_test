'''
문자열에서 부분 문자열을 검색하는 알고리즘으로는 
- 브루트 포스법
- KMP 법
- 보이어.무어법 
등이 있다.

여기서는 브루트 포스법을 배워보자

문자열 검색이란, 문자열에서 어떤 문자열이 있는지 검사하고, 있다면 어디에 위치하는지 찾아내는 것.
- 검색 당하는 애: 텍스트
- 우리가 찾고 싶은 애: 패턴
즉, 텍스트에서 패턴을 찾아낸다.

문자열 검색 알고리즘 중에서 가장 기초적이고 단순한 것이 브루트 포스법이다.
브루트 포스법은 선형 검색을 단순히 확장한 것이라 '단순법'이라고도 한다. 
'''

def bf_match(txt: str, pat: str) -> int:
    pt = pp = 0
    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        else:
            pt = pt - pp + 1
            pp = 0
    return pt - pp if pp == len(pat) else -1

if __name__ == '__main__':
    s1 = input('text input: ')
    s2 = input('pattern input: ')
    idx = bf_match(s1, s2)
    if idx == -1:
        print('no pattern in text')
    else:
        print(f'match in {idx} index')