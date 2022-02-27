from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None: #뮤타블 시퀀스를 그냥 바꿔주고 끝내면 되니까 리턴이 필요가 없음
    for i in range(len(a) // 2):
        a[i], a[-(i+1)] =  a[-(i+1)], a[i]

if __name__ == '__main__':
    print("배열 원소를 역순으로 정렬합니다.")
    num = int(input("원소 수를 입력하세요: "))
    
    l = []
    for i in range(num): l.append(int(input(f"x[{i}]값을 입력하세요: ")))
    
    reverse_array(l)
    print("배열 원소를 역순으로 정렬했습니다.")

    for j in range(num): print(f"x[{j}] = {l[j]}")


    

