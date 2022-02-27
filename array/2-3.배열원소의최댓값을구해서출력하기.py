# 원솟값을 End 나올때까지 입력 받음
l = []
count = 0

while True:
    n = input("input number, to stop type End: ")
    if n == 'End':
        break
    l.append(int(n))
    count += 1
print(max(l))
print(count)
