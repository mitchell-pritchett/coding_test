# 모든 수로 나눌 필요가 없다.
# 어떤 수가 2,3으로 나눠지지 않는다면 당연히 2의 배수나 3의 배수로도 나눠지지 않는다.
# 따라서 우린 그 수보다 작은 소수들로 안나눠지는지만 보면 된다.

counter = 0
prime = [2]

for n in range(3, 1001, 2):
    for i in prime[1:]:
        counter += 1
        if n % i == 0: # not prime
            break
    else:
        prime.append(n)

for pr in prime:
    print(pr)
print(len(prime))
print("나눗셈 횟수:", counter)

