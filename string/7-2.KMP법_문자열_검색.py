def kmp_match(txt: str, pat: str) -> int:
    pt = 1
    pp = 0
    skip = [0] * (len(pat) + 1)

    skip[pt] = 0
    while pt != len(pat):
        if pat[pt] == pat[pp]:
            pt += 1
            pp += 1
            skip[pt] = pp
        elif pp == 0:
            pt += 1
            skip[pt] = pp
        else:
            pp = skip[pp]

    pt = pp = 0
    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        elif pp == 0:
            pt += 1
        else:
            pp = skip[pp]
    
    return pt - pp if pp == len(pat) else -1

if __name__ == '__main__':
    s1 = input('text input: ')
    s2 = input('pattern input: ')

    idx = kmp_match(s1, s2)

    if idx == -1:
        print("no pattern in text")
    else:
        print(f"pattern starts in index {idx}")