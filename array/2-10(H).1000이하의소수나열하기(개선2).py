<<<<<<< HEAD
counter = 0
prime = [None] * 500
ptr = 0

prime[ptr] = 2
ptr += 1
prime[ptr] = 3
ptr += 1

for n in range(5, 1001, 2):
    i = 1
    while prime[i] * prime[i] <= n:
        counter += 2
        if n % prime[i] == 0:
            break
        i += 1
    else:
        prime[ptr] = n
        ptr += 1
        counter += 1

for i in range(ptr):
    print(prime[i])

=======
counter = 0
prime = [None] * 500
ptr = 0

prime[ptr] = 2
ptr += 1
prime[ptr] = 3
ptr += 1

for n in range(5, 1001, 2):
    i = 1
    while prime[i] * prime[i] <= n:
        counter += 2
        if n % prime[i] == 0:
            break
        i += 1
    else:
        prime[ptr] = n
        ptr += 1
        counter += 1

for i in range(ptr):
    print(prime[i])

>>>>>>> 2d8319d170ef6f026fca7327b39a71e5297cfca9
print('나눗셈 횟수:', counter)