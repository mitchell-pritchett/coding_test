n = int(input("how many integers to save?: "))
a = [None] * n

cnt = 0
while True:
    a[cnt % n] = int(input(f'{cnt + 1}번째 정수를 입력하세요: '))
    cnt += 1

    retry = input("continue? (y/n): ")
    if retry in 'Nn':
        break

i = cnt - n
if i < 0: i = 0 # cnt 보다 n(저장가능수)가 많으면, 가장 오래된 거는 0번째 인덱스에 있음
# 같으면 i = 0이고,
# cnt > n 이면 예를 들어 저장 가능 수가 4고 cnt = 5면 i = 1 가장 오랜된 거 인덱스

while i < cnt:
    print(f"{i + 1}번째 = {a[i % n]}") 
    i += 1



